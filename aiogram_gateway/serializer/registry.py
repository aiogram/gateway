from typing import Any

from aiogram_gateway.serializer.serializer import Serializer


class Registry:
    def __init__(self, serializers: dict[Any: Serializer]) -> None:
        self._serializers = {}

        for type_, serializer in serializers.items():
            self.register(type_, serializer)

    def register[S, D](self, type_: S, serializer: Serializer[S, D]) -> None:
        self._serializers[type_] = serializer

    def get(self, type_: type) -> Serializer:
        try:
            return self._serializers[type_]
        except KeyError:
            raise ValueError(f"No serializer found for {type_}")

    def serialize[S, D](self, obj: S, type_: type[S] | None = None) -> D:
        if type_ is None:
            type_ = type(obj)
        serializer = self.get(type_)
        return serializer.serialize(self, obj)

    def deserialize[S, D](self, obj: D, type_: type[S] | None = None) -> S:
        if type_ is None:
            type_ = type(obj)
        serializer = self.get(type_)
        return serializer.deserialize(self, obj)

