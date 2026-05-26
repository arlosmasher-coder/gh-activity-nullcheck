"""
gh_activity_nullcheck - Detect missing GitHub activity signals and explain likely configuration or visibility causes.
"""

__version__ = "0.1.0"

from .heuristics_for_privaterepo_and import GhActivityNullcheck
from .types import GhActivityNullcheckOptions, GhActivityNullcheckResult
from .exceptions import GhActivityNullcheckError, ConfigurationError, ValidationError

__all__ = [
    "GhActivityNullcheck",
    "GhActivityNullcheckOptions",
    "GhActivityNullcheckResult",
    "GhActivityNullcheckError",
    "ConfigurationError",
    "ValidationError",
]
