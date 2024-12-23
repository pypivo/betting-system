from aio_pika import Message, connect, ExchangeType

from src.common.helpers import json_dumps


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

    async def publish(self, message_body: dict, routing_key: str):
        if not self.exchange:
            raise RuntimeError("QueueManager is not initialized. Call `initialize` first.")

        message = Message(json_dumps(message_body).encode())
        await self.exchange.publish(message, routing_key=routing_key)

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
