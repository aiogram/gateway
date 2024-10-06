from datetime import datetime

from aiogram_gateway.serializer.registry import Registry
from aiogram_gateway.serializer.serializer import Serializer


class DateTimeSerializer(Serializer[datetime, int]):
    def serialize(self, registry: Registry, obj: datetime) -> int:
        return round(obj.timestamp())

    def deserialize(self, registry: Registry, obj: int) -> datetime:
        return datetime.fromtimestamp(obj)
