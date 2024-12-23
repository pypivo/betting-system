from aio_pika import connect, ExchangeType

from src.rpc.routes import RpcRouters, EventRpcRouter


class RpcManager:
    def __init__(self, rabbitmq_url, exchange_name, exchange_type=ExchangeType.TOPIC):
        self.rabbitmq_url = rabbitmq_url
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.connection = None
        self.channel = None
        self.exchange = None

    async def initialize(self):
        
        self.connection = await connect(self.rabbitmq_url)
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            self.exchange_name, self.exchange_type
        )

    async def consume(self, callback, queue_name=None):
        if not self.channel:
            raise RuntimeError("QueueManager is not initialized. Call `initialize` first.")

        if queue_name:
            queue = await self.channel.declare_queue(queue_name, durable=True)
        else:
            queue = await self.channel.declare_queue(exclusive=True)

        await queue.bind(self.exchange, routing_key=queue_name)
        await queue.consume(callback)

    async def close(self):
        if self.connection:
            await self.connection.close()


async def init_rpc_manager(
    rabbitmq_url: str,
    exchange_name: str,
    exchange_type: ExchangeType = ExchangeType.TOPIC
) -> RpcManager:
    rpc_manager = RpcManager(rabbitmq_url, exchange_name, exchange_type)
    await rpc_manager.initialize()
    return rpc_manager


async def bind(rpc_manager: RpcManager, event_rpc_router: EventRpcRouter):
    rpc_method_map = {
        RpcRouters.notification_event_status_updated: event_rpc_router.update_event_status,
        RpcRouters.notification_event_created: event_rpc_router.create_event,
    }

    for method, handler in rpc_method_map.items():
        await rpc_manager.consume(callback=handler, queue_name=method)
