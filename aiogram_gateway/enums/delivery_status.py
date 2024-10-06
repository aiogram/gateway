from enum import StrEnum


class DeliveryStatusEnum(StrEnum):
    SENT = "sent"
    """The message has been sent to the recipient's device(s)."""
    READ = "read"
    """The message has been read by the recipient."""
    REVOKED = "revoked"
    """The message has been revoked."""
