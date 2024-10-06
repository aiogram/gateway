from dataclasses import dataclass
from typing import Any

from aiogram_gateway.serializer.registry import Registry
from aiogram_gateway.serializer.serializer import Serializer
from aiogram_gateway.types.base import TelegramGatewayObject
from aiogram_gateway.types.delivery_status import DeliveryStatus
from aiogram_gateway.types.verification_status import VerificationStatus


@dataclass(frozen=True, slots=True, kw_only=True)
class RequestStatus(TelegramGatewayObject):
    """
    This object represents the status of a verification message request.

    Source: https://core.telegram.org/gateway/api#requeststatus
    """

    request_id: str
    """Unique identifier of the verification request."""
    phone_number: str
    """The phone number to which the verification code was sent, in the E.164 format."""
    request_cost: float
    """Total request cost incurred by either checkSendAbility or sendVerificationMessage."""
    remaining_balance: float | None = None
    """Optional. Remaining balance in credits. Returned only in response to a request that incurs a charge."""
    delivery_status: DeliveryStatus | None = None
    """Optional. The current message delivery status. Returned only if a verification message was sent to the user."""
    verification_status: VerificationStatus | None = None
    """Optional. The current status of the verification process."""
    payload: str | None = None
    """Optional. Custom payload if it was provided in the request, 0-256 bytes."""


class RequestStatusSerializer(Serializer[RequestStatus, dict[str, Any]]):
    def serialize(self, registry: Registry, obj: RequestStatus) -> dict[str, Any]:
        data = {
            "request_id": obj.request_id,
            "phone_number": obj.phone_number,
            "request_cost": obj.request_cost,
        }
        if obj.remaining_balance is not None:
            data["remaining_balance"] = obj.remaining_balance
        if obj.delivery_status is not None:
            data["delivery_status"] = registry.serialize(obj.delivery_status)
        if obj.verification_status is not None:
            data["verification_status"] = registry.serialize(obj.verification_status)
        if obj.payload is not None:
            data["payload"] = obj.payload
        return data

    def deserialize(self, registry: Registry, data: dict[str, Any]) -> RequestStatus:
        return RequestStatus(
            request_id=data["request_id"],
            phone_number=data["phone_number"],
            request_cost=data["request_cost"],
            remaining_balance=data.get("remaining_balance"),
            delivery_status=registry.deserialize(data.get("delivery_status"), DeliveryStatus) if data.get(
                "delivery_status") else None,
            verification_status=registry.deserialize(data.get("verification_status"), VerificationStatus) if data.get(
                "verification_status") else None,
            payload=data.get("payload"),
        )
