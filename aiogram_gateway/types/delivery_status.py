from dataclasses import dataclass
from datetime import datetime
from typing import Any

from aiogram_gateway.enums.delivery_status import DeliveryStatusEnum
from aiogram_gateway.serializer.registry import Registry
from aiogram_gateway.serializer.serializer import Serializer
from aiogram_gateway.types.base import TelegramGatewayObject


@dataclass(frozen=True, slots=True, kw_only=True)
class DeliveryStatus(TelegramGatewayObject):
    """
    This object represents the status of a message delivery.

    Source: https://core.telegram.org/gateway/api#deliverystatus
    """

    status: DeliveryStatusEnum
    """The current status of the message."""
    updated_at: datetime
    """The timestamp when the status was last updated."""


class DeliveryStatusSerializer(Serializer[DeliveryStatus, dict[str, Any]]):
    def serialize(self, registry: Registry, obj: DeliveryStatus) -> dict[str, Any]:
        return {
            "status": registry.serialize(obj.status, DeliveryStatus),
            "updated_at": registry.serialize(obj.updated_at, datetime),
        }

    def deserialize(self, registry: Registry, data: dict[str, Any]) -> DeliveryStatus:
        return DeliveryStatus(
            status=registry.deserialize(data["status"], DeliveryStatusEnum),
            updated_at=registry.deserialize(data["updated_at"], datetime),
        )
