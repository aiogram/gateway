from enum import StrEnum


class VerificationStatusEnum(StrEnum):
    VERIFIED = "verified"
    """The user is verified."""
    UNVERIFIED = "unverified"
    """The user is not verified."""
    PENDING = "pending"
    """The user's verification is pending."""
    REJECTED = "rejected"
    """The user's verification has been rejected."""
    ERROR = "error"
    """An error occurred while verifying the user."""
    UNKNOWN = "unknown"
    """The user's verification status is unknown."""
