# ABOUTME: Implementation of 'ethica frameworks' command group
# ABOUTME: Lists and inspects available ethics frameworks

"""
Manage and inspect ethics frameworks.
"""

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from ethica.core.registry import FrameworkRegistry

app = typer.Typer(help="Manage ethics frameworks")
console = Console()


@app.command("list")
def list_frameworks() -> None:
    """List all available frameworks"""

    registry = FrameworkRegistry()
    frameworks = registry.list_frameworks()

    if not frameworks:
        console.print("[yellow]No frameworks found[/yellow]")
        return

    table = Table(title="Available Ethics Frameworks", show_header=True)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Name", style="bold")
    table.add_column("Version")
    table.add_column("Category")
    table.add_column("Status", style="green")

    for fw in frameworks:
        table.add_row(
            fw["id"],
            fw["name"],
            fw.get("version", "N/A"),
            fw.get("category", "N/A"),
            fw.get("status", "available"),
        )

    console.print(table)
    console.print(
        f"\nUse [cyan]ethica frameworks info <id>[/cyan] for detailed information"
    )


@app.command("info")
def framework_info(framework_id: str) -> None:
    """Show detailed information about a framework"""

    registry = FrameworkRegistry()

    try:
        framework_spec = registry.load_framework_spec(framework_id)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1)

    # Framework metadata
    metadata = framework_spec["metadata"]
    console.print(f"\n[bold cyan]{metadata['name']}[/bold cyan]")
    console.print(f"[dim]{metadata['description']}[/dim]\n")

    console.print(f"[bold]Version:[/bold] {metadata['version']}")
    console.print(f"[bold]ID:[/bold] {metadata['id']}")
    console.print(f"[bold]License:[/bold] {metadata.get('license', 'N/A')}")
    console.print(f"[bold]Maintainer:[/bold] {metadata.get('maintainer', 'N/A')}")

    if metadata.get("source_url"):
        console.print(f"[bold]Source:[/bold] {metadata['source_url']}")

    # Principles
    console.print(f"\n[bold]Principles ({len(framework_spec['principles'])}):[/bold]")
    for principle in framework_spec["principles"]:
        console.print(f"  • [cyan]{principle['name']}[/cyan] ({principle['weight']})")

    # Checks
    total_checks = len(framework_spec["checks"])
    error_checks = sum(1 for c in framework_spec["checks"] if c["severity"] == "error")
    warning_checks = sum(1 for c in framework_spec["checks"] if c["severity"] == "warning")

    console.print(f"\n[bold]Checks ({total_checks} total):[/bold]")
    console.print(f"  • Required (errors): {error_checks}")
    console.print(f"  • Recommended (warnings): {warning_checks}")

    # Compliance levels
    if "compliance_levels" in framework_spec:
        console.print(f"\n[bold]Compliance Levels:[/bold]")
        for level_id, level in framework_spec["compliance_levels"].items():
            console.print(f"  • [cyan]{level['name']}[/cyan]: {level['description']}")


@app.command("validate")
def validate_framework(framework_file: str) -> None:
    """Validate a custom framework YAML file"""

    from pathlib import Path

    path = Path(framework_file)
    if not path.exists():
        console.print(f"[red]Error:[/red] File not found: {framework_file}")
        raise typer.Exit(1)

    # TODO: Implement schema validation
    console.print("[yellow]Framework validation not yet implemented[/yellow]")
