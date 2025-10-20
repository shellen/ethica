# ABOUTME: Dependency-based compliance checks for Python packages
# ABOUTME: Checks requirements.txt, pyproject.toml, and setup.py for required libraries

"""
Dependency-based compliance checks.
"""

import re
from pathlib import Path
from typing import Set

from ethics_ai.checks.base import BaseCheck, CheckResult, CheckStatus


class DependencyCheck(BaseCheck):
    """Check if required packages are declared as dependencies"""

    def run(self, project_path: Path) -> CheckResult:
        """
        Check if required packages are in project dependencies.

        Config:
            packages: List of package names to check for
            require_any: If True, at least one package must be present (default)
            require_all: If True, all packages must be present
        """
        packages = self.config.get("packages", [])
        require_any = self.config.get("require_any", True)
        require_all = self.config.get("require_all", False)

        if not packages:
            return self._create_result(
                CheckStatus.SKIPPED,
                "No packages configured for check",
            )

        # Get all declared dependencies
        declared_deps = self._get_project_dependencies(project_path)

        # Check which required packages are present
        found_packages = [pkg for pkg in packages if pkg.lower() in declared_deps]

        # Evaluate result based on requirements
        if require_all:
            if len(found_packages) == len(packages):
                return self._create_result(
                    CheckStatus.PASSED,
                    f"All required packages found: {', '.join(found_packages)}",
                )
            else:
                missing = [pkg for pkg in packages if pkg.lower() not in declared_deps]
                return self._create_result(
                    CheckStatus.FAILED,
                    f"Missing required packages: {', '.join(missing)}",
                    suggestion=f"Install: {', '.join(missing)}",
                )
        else:  # require_any (default)
            if found_packages:
                return self._create_result(
                    CheckStatus.PASSED,
                    f"Found package(s): {', '.join(found_packages)}",
                )
            else:
                packages_formatted = ", ".join(packages)
                return self._create_result(
                    CheckStatus.FAILED,
                    f"No required packages found. Expected at least one of: {packages_formatted}",
                    suggestion=f"Install one of: {packages_formatted}",
                )

    def _get_project_dependencies(self, project_path: Path) -> Set[str]:
        """
        Extract all declared dependencies from project files.

        Returns:
            Set of lowercase package names
        """
        dependencies: Set[str] = set()

        # Check requirements.txt
        requirements_files = [
            "requirements.txt",
            "requirements-dev.txt",
            "requirements/base.txt",
            "requirements/dev.txt",
        ]

        for req_file in requirements_files:
            req_path = project_path / req_file
            if req_path.exists():
                dependencies.update(self._parse_requirements_file(req_path))

        # Check pyproject.toml
        pyproject_path = project_path / "pyproject.toml"
        if pyproject_path.exists():
            dependencies.update(self._parse_pyproject_toml(pyproject_path))

        # Check setup.py
        setup_path = project_path / "setup.py"
        if setup_path.exists():
            dependencies.update(self._parse_setup_py(setup_path))

        return dependencies

    def _parse_requirements_file(self, file_path: Path) -> Set[str]:
        """Parse requirements.txt style file"""
        dependencies = set()

        try:
            content = file_path.read_text()
            for line in content.splitlines():
                line = line.strip()
                # Skip comments and empty lines
                if not line or line.startswith("#"):
                    continue
                # Extract package name (before ==, >=, etc.)
                match = re.match(r"([a-zA-Z0-9_-]+)", line)
                if match:
                    dependencies.add(match.group(1).lower())
        except Exception:
            pass

        return dependencies

    def _parse_pyproject_toml(self, file_path: Path) -> Set[str]:
        """Parse pyproject.toml for dependencies"""
        dependencies = set()

        try:
            content = file_path.read_text()

            # Simple pattern matching for dependencies
            # This is a basic implementation; a full parser would be more robust
            in_dependencies = False
            for line in content.splitlines():
                line = line.strip()

                # Detect dependency sections
                if line.startswith("[") and "dependencies" in line.lower():
                    in_dependencies = True
                    continue
                elif line.startswith("["):
                    in_dependencies = False
                    continue

                if in_dependencies and "=" in line:
                    # Extract package name from entries like: 'package = ">=1.0"'
                    match = re.match(r'"?([a-zA-Z0-9_-]+)"?\s*=', line)
                    if match:
                        dependencies.add(match.group(1).lower())

                # Also check for dependencies array format
                if "dependencies = [" in line or in_dependencies:
                    matches = re.findall(r'"([a-zA-Z0-9_-]+)[>=<]', line)
                    for match in matches:
                        dependencies.add(match.lower())

        except Exception:
            pass

        return dependencies

    def _parse_setup_py(self, file_path: Path) -> Set[str]:
        """Parse setup.py for dependencies"""
        dependencies = set()

        try:
            content = file_path.read_text()

            # Look for install_requires
            matches = re.findall(
                r'install_requires\s*=\s*\[(.*?)\]',
                content,
                re.DOTALL
            )

            for match in matches:
                # Extract package names
                packages = re.findall(r'"([a-zA-Z0-9_-]+)[>=<]?', match)
                dependencies.update(pkg.lower() for pkg in packages)

        except Exception:
            pass

        return dependencies
