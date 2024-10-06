from dataclasses import dataclass
from datetime import datetime

from aiogram_gateway.enums.verification_status import VerificationStatusEnum
from aiogram_gateway.serializer.registry import Registry
from aiogram_gateway.serializer.serializer import Serializer
from aiogram_gateway.types.base import TelegramGatewayObject


@dataclass(frozen=True, slots=True, kw_only=True)
class VerificationStatus(TelegramGatewayObject):
    """
    This object represents the verification status of a code.

    Source: https://core.telegram.org/gateway/api#verificationstatus
    """
    status: VerificationStatusEnum
    """The current status of the verification process."""
    updated_at: datetime
    """The timestamp when the status was last updated."""
    code_entered: str
    """The code entered by the user."""


class VerificationStatusSerializer(Serializer[VerificationStatus, dict[str, str]]):
    def serialize(self, registry: Registry, obj: VerificationStatus) -> dict[str, str]:
        return {
            "status": obj.status.value,
            "updated_at": registry.serialize(obj.updated_at, datetime),
            "code_entered": obj.code_entered,
        }

    def deserialize(self, registry: Registry, data: dict[str, str]) -> VerificationStatus:
        return VerificationStatus(
            status=registry.deserialize(data["status"], VerificationStatusEnum),
            updated_at=registry.deserialize(data["updated_at"], datetime),
            code_entered=data["code_entered"],
        )
