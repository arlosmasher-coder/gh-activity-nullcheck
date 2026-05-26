"""Type definitions for gh_activity_nullcheck."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class GhActivityNullcheckOptions:
    """Configuration options for GhActivityNullcheck.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Heuristics for private-repo and org-visibility scenarios
        feature_2: Configuration for: Confidence-scored explanations and remediation hints
        feature_3: Configuration for: Batch processing for lists of usernames
        feature_4: Configuration for: Export to CSV/JSON for downstream systems
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None


@dataclass
class GhActivityNullcheckResult:
    """Result returned by GhActivityNullcheck operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
