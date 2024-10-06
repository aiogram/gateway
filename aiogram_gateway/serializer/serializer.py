from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram_gateway.serializer.registry import Registry


class Serializer[S, D](ABC):
    def serialize(self, registry: Registry, obj: S) -> D:
        pass

    def deserialize(self, registry: Registry, obj: D) -> S:
        pass
