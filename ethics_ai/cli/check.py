# ABOUTME: Implementation of 'ethics-ai check' command
# ABOUTME: Runs compliance checks and displays results

"""
Run ethics compliance checks on a project.
"""

from pathlib import Path
from typing import Optional

import typer
import yaml
from rich.console import Console
from rich.table import Table

from ethics_ai.core.checker import CheckEngine
from ethics_ai.core.registry import FrameworkRegistry

console = Console()


def check_command(
    framework: Optional[str] = typer.Option(
        None,
        "--framework",
        "-f",
        help="Override framework from config",
    ),
    level: Optional[str] = typer.Option(
        None,
        "--level",
        "-l",
        help="Override compliance level from config",
    ),
    output: str = typer.Option(
        "text",
        "--output",
        "-o",
        help="Output format (text, json)",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show detailed output",
    ),
) -> None:
    """Run ethics compliance checks on your project"""

    # Load project configuration
    config_path = Path(".ai-ethics.yaml")
    if not config_path.exists():
        console.print(
            "[red]Error:[/red] No .ai-ethics.yaml found. "
            "Run [cyan]ethics-ai init[/cyan] first."
        )
        raise typer.Exit(1)

    with open(config_path) as f:
        config = yaml.safe_load(f)

    # Get framework to check
    framework_id = framework or config["frameworks"][0]["id"]
    compliance_level = level or config["frameworks"][0]["compliance_level"]

    # Load framework and run checks
    registry = FrameworkRegistry()
    framework_spec = registry.load_framework_spec(framework_id)

    console.print(f"\nChecking against [cyan]{framework_id}[/cyan] ({compliance_level} level)...\n")

    # Run checks
    engine = CheckEngine(framework_spec)
    results = engine.run_checks(Path.cwd())

    # Display results
    if output == "text":
        _display_text_results(results, framework_spec, verbose)
    elif output == "json":
        _display_json_results(results)
    else:
        console.print(f"[red]Error:[/red] Unknown output format: {output}")
        raise typer.Exit(1)

    # Exit with error code if checks failed
    total_failed = sum(
        1 for principle in results["principles"]
        for check in principle["checks"]
        if check["status"] == "failed" and check["severity"] == "error"
    )

    if total_failed > 0:
        raise typer.Exit(1)


def _display_text_results(results: dict, framework_spec: dict, verbose: bool) -> None:
    """Display results in text format"""

    for principle in results["principles"]:
        # Get principle details from spec
        principle_spec = next(
            (p for p in framework_spec["principles"] if p["id"] == principle["id"]),
            None
        )

        # Principle header
        status_icon = "✓" if principle["status"] == "passed" else "✗"
        status_color = "green" if principle["status"] == "passed" else "red"

        console.print(
            f"[bold]{principle_spec['name']}[/bold] "
            f"[{status_color}]{status_icon}[/{status_color}]"
        )

        # Show checks
        for check in principle["checks"]:
            if check["status"] == "passed":
                if verbose:
                    console.print(f"  [green]✓[/green] {check['name']}: {check['message']}")
            elif check["status"] == "failed":
                severity_color = "red" if check["severity"] == "error" else "yellow"
                console.print(
                    f"  [{severity_color}]✗[/{severity_color}] {check['name']}: {check['message']}"
                )
                if check.get("suggestion"):
                    console.print(f"    [dim]→ {check['suggestion']}[/dim]")
            elif check["status"] == "skipped":
                if verbose:
                    console.print(f"  [dim]○ {check['name']}: {check['message']}[/dim]")

        console.print()

    # Summary
    console.print(f"\n[bold]Summary:[/bold]")
    console.print(f"Overall Status: [{results['overall_status_color']}]{results['overall_status']}[/{results['overall_status_color']}]")
    console.print(f"Pass Rate: {results['pass_rate']:.1%}")
    console.print(f"Checks Passed: {results['checks_passed']}/{results['total_checks']}")

    if results["overall_status"] != "passed":
        console.print(f"\n[yellow]Run with --verbose to see all check details[/yellow]")


def _display_json_results(results: dict) -> None:
    """Display results in JSON format"""
    import json

    console.print(json.dumps(results, indent=2))
