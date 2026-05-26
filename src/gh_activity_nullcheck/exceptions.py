"""Custom exceptions for gh_activity_nullcheck."""

from __future__ import annotations


class GhActivityNullcheckError(Exception):
    """Base exception for all GhActivityNullcheck errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(GhActivityNullcheckError):
    """Raised when the SDK is misconfigured."""


class ValidationError(GhActivityNullcheckError):
    """Raised when input validation fails."""


class TimeoutError(GhActivityNullcheckError):
    """Raised when an operation exceeds its time limit."""
