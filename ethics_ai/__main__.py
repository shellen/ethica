# ABOUTME: CLI entry point for ethics-ai command
# ABOUTME: Sets up typer app and registers all command groups

"""
Main CLI entry point for ethics-ai-commons.
"""

import typer
from rich.console import Console

from ethics_ai.cli import init, check, frameworks

app = typer.Typer(
    name="ethics-ai",
    help="Framework-agnostic platform for AI ethics compliance checking",
    no_args_is_help=True,
)

console = Console()

# Register command groups
app.command(name="init")(init.init_command)
app.command(name="check")(check.check_command)
app.add_typer(frameworks.app, name="frameworks")


@app.command()
def version() -> None:
    """Show version information"""
    from ethics_ai import __version__

    console.print(f"ethics-ai version {__version__}")


def main() -> None:
    """Main entry point"""
    app()


if __name__ == "__main__":
    main()
