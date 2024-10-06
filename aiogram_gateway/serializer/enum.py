from aiogram_gateway.serializer.registry import Registry
from aiogram_gateway.serializer.serializer import Serializer


class StrEnumSerializer[T](Serializer[T, str]):
    def __init__(self, enum: type[T]) -> None:
        self.enum = enum

    def serialize(self,registry: Registry,  obj: T) -> str:
        return obj.value

    def deserialize(self, registry: Registry, obj: str) -> T:
        return self.enum(obj)
