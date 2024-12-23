from functools import wraps
import uuid
from datetime import date, datetime
from typing import Any, Callable, Type

from pydantic import BaseModel, ValidationError
import ujson
from fastapi.encoders import jsonable_encoder


class Stub:
    def __init__(self, dependency: Callable[..., Any]) -> None:
        self._dependency = dependency

    def __call__(self) -> None:
        raise NotImplementedError(f"You forgot to register `{self._dependency}` implementation.")

    def __hash__(self) -> int:
        return hash(self._dependency)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Stub):
            return self._dependency == __value._dependency
        else:
            return self._dependency == __value


def rpc_wrapper(schema: Type[BaseModel]):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(self, message: dict, *args, **kwargs):
            try:
                if hasattr(message, "body"):
                    body = json_loads(message.body)
                else:
                    body = message

                parsed_message = schema.model_validate(body)
            except ValidationError as e:
                raise ValueError(f"Invalid input data: {e}")

            return await func(self, parsed_message, *args, **kwargs)

        return wrapper
    return decorator


def json_dumps_default(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    elif isinstance(value, date):
        return value.isoformat()
    else:
        return jsonable_encoder(value)


def json_dumps(data: Any) -> str:
    return ujson.dumps(data, ensure_ascii=False, default=json_dumps_default)


def json_loads(data: str) -> dict[Any, Any]:
    return ujson.loads(data)


def utcnow() -> datetime:
    return datetime.utcnow()


def str_uuid() -> str:
    return str(uuid.uuid4())
