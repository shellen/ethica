# ABOUTME: File-based compliance checks (existence, content patterns)
# ABOUTME: Checks for required documentation and configuration files

"""
File-based compliance checks.
"""

from pathlib import Path

from ethica.checks.base import BaseCheck, CheckResult, CheckStatus


class FileExistsCheck(BaseCheck):
    """Check if specified files or directories exist"""

    def run(self, project_path: Path) -> CheckResult:
        """
        Check if any of the specified paths exist.

        Config:
            paths: List of file/directory paths to check
        """
        paths = self.config.get("paths", [])

        if not paths:
            return self._create_result(
                CheckStatus.SKIPPED,
                "No paths configured for check",
            )

        # Check each path
        for path_str in paths:
            full_path = project_path / path_str
            if full_path.exists():
                return self._create_result(
                    CheckStatus.PASSED,
                    f"Found required file/directory at {path_str}",
                )

        # None found
        paths_formatted = ", ".join(paths)
        suggestion = f"Create one of: {paths_formatted}"

        if self.help_url:
            suggestion += f"\nSee: {self.help_url}"

        return self._create_result(
            CheckStatus.FAILED,
            f"Required file/directory not found. Expected one of: {paths_formatted}",
            suggestion=suggestion,
        )
