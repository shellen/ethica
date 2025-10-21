# ABOUTME: Base classes for ethics compliance checks
# ABOUTME: Defines check interface, status, severity, and result types

"""
Base classes and types for ethics compliance checks.
"""

from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
from typing import Any, Optional


class CheckSeverity(Enum):
    """Severity level of a check"""

    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class CheckStatus(Enum):
    """Result status of a check"""

    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"


class CheckResult:
    """Result of running a compliance check"""

    def __init__(
        self,
        check_id: str,
        name: str,
        status: CheckStatus,
        message: str,
        severity: CheckSeverity,
        suggestion: Optional[str] = None,
    ) -> None:
        self.check_id = check_id
        self.name = name
        self.status = status
        self.message = message
        self.severity = severity
        self.suggestion = suggestion

    def to_dict(self) -> dict[str, Any]:
        """Convert result to dictionary"""
        return {
            "id": self.check_id,
            "name": self.name,
            "status": self.status.value,
            "message": self.message,
            "severity": self.severity.value,
            "suggestion": self.suggestion,
        }


class BaseCheck(ABC):
    """Base class for all compliance checks"""

    def __init__(self, check_spec: dict[str, Any]) -> None:
        """
        Initialize check from specification.

        Args:
            check_spec: Check specification from framework YAML
        """
        self.check_id = check_spec["id"]
        self.name = check_spec["name"]
        self.principle = check_spec["principle"]
        self.severity = CheckSeverity(check_spec["severity"])
        self.description = check_spec["description"]
        self.config = check_spec.get("config", {})
        self.help_url = check_spec.get("help_url")

    @abstractmethod
    def run(self, project_path: Path) -> CheckResult:
        """
        Execute the check.

        Args:
            project_path: Path to the project directory

        Returns:
            CheckResult with status and details
        """
        pass

    def _create_result(
        self,
        status: CheckStatus,
        message: str,
        suggestion: Optional[str] = None,
    ) -> CheckResult:
        """Helper to create a CheckResult"""
        return CheckResult(
            check_id=self.check_id,
            name=self.name,
            status=status,
            message=message,
            severity=self.severity,
            suggestion=suggestion,
        )
