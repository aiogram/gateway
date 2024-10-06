from datetime import datetime

from aiogram_gateway.enums.delivery_status import DeliveryStatusEnum
from aiogram_gateway.enums.verification_status import VerificationStatusEnum
from aiogram_gateway.serializer.datetime import DateTimeSerializer
from aiogram_gateway.serializer.enum import StrEnumSerializer
from aiogram_gateway.serializer.registry import Registry
from aiogram_gateway.types.delivery_status import DeliveryStatus, DeliveryStatusSerializer
from aiogram_gateway.types.request_status import RequestStatusSerializer, RequestStatus
from aiogram_gateway.types.verification_status import VerificationStatusSerializer, VerificationStatus

DEFAULT_SERIALIZERS = {
    datetime: DateTimeSerializer(),
    DeliveryStatusEnum: StrEnumSerializer(DeliveryStatusEnum),
    VerificationStatusEnum: StrEnumSerializer(VerificationStatusEnum),
    DeliveryStatus: DeliveryStatusSerializer(),
    RequestStatus: RequestStatusSerializer(),
    VerificationStatus: VerificationStatusSerializer(),
}

DEFAULT_REGISTRY = Registry(DEFAULT_SERIALIZERS)
