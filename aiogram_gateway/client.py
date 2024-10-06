from datetime import timedelta
from typing import Any
from urllib.parse import urljoin

from aiohttp import ClientSession, FormData

from aiogram_gateway.serializer.default import DEFAULT_REGISTRY
from aiogram_gateway.serializer.registry import Registry
from aiogram_gateway.types.request_status import RequestStatus

BASE_URL = "https://gatewayapi.telegram.org"


class TelegramGateway:
    def __init__(self, access_token: str, timeout: float = 60.0, base_url: str = BASE_URL,
                 serializers: Registry = DEFAULT_REGISTRY, ) -> None:
        self.access_token = access_token
        self.timeout = timeout
        self.base_url = base_url
        self.serializers = serializers

    async def _emit(self, method: str, data: dict[str, Any]) -> dict[str, Any]:
        async with ClientSession() as session:
            url = urljoin(self.base_url, method)
            headers = {
                "Authorization": f"Bearer {self.access_token}",
            }
            form = FormData()
            for key, value in data.items():
                form.add_field(key, value)

            async with session.post(url, headers=headers, data=form, timeout=self.timeout) as response:
                response.raise_for_status()

                result = await response.json()
                if result['ok'] is False:
                    raise ValueError(result)
                print(f"{method} -> {result}")
                return result["result"]

    async def send_verification_message(
            self,
            phone_number: str,
            request_id: str | None = None,
            sender_username: str | None = None,
            code: str | None = None,
            code_length: int | None = None,
            callback_url: str | None = None,
            payload: str | None = None,
            ttl: int | timedelta | None = None,
    ) -> RequestStatus:
        """
        Send a verification message to the specified phone number.

        Source: https://core.telegram.org/gateway/api
        """
        data = {
            "phone_number": phone_number,
        }

        if request_id is not None:
            data["request_id"] = request_id
        if sender_username is not None:
            data["sender_username"] = sender_username
        if code is not None:
            data["code"] = code
        if code_length is not None:
            data["code_length"] = code_length
        if callback_url is not None:
            data["callback_url"] = callback_url
        if payload is not None:
            data["payload"] = payload
        if ttl is not None:
            if isinstance(ttl, timedelta):
                ttl = round(ttl.total_seconds())
            data["ttl"] = ttl

        result = await self._emit("sendVerificationMessage", data)
        return self.serializers.deserialize(result, RequestStatus)

    async def check_send_ability(self,
                                 phone_number: str,
                                 ) -> RequestStatus:
        """
        Check the ability to send a verification message to the specified phone number.

        Source: https://core.telegram.org/gateway/api
        """
        data = {
            "phone_number": phone_number,
        }

        result = await self._emit("checkSendAbility", data)
        return self.serializers.deserialize(result, RequestStatus)

    async def check_verification_status(self,
                                        request_id: str,
                                        code: str | None = None) -> RequestStatus:
        """
        Check the verification status of the specified request.

        :param request_id:
        :param code:
        :return:
        """
        data = {
            "request_id": request_id,
        }

        if code is not None:
            data["code"] = code

        result = await self._emit("checkVerificationStatus", data)
        return self.serializers.deserialize(result, RequestStatus)

    async def revoke_verification_message(self, request_id: str) -> RequestStatus:
        """
        Revoke the verification message request.

        :param request_id:
        :return:
        """
        data = {
            "request_id": request_id,
        }

        result = await self._emit("revokeVerificationMessage", data)
        return self.serializers.deserialize(result, RequestStatus)
