# ABOUTME: Implementation of 'ethica init' command
# ABOUTME: Initializes AI ethics compliance in a project

"""
Initialize ethics compliance configuration in a project.
"""

from pathlib import Path
from typing import Optional

import typer
import yaml
from rich.console import Console
from rich.panel import Panel

console = Console()


def init_command(
    framework: str = typer.Option(
        "unesco-2021",
        "--framework",
        "-f",
        help="Framework to initialize with",
    ),
    level: str = typer.Option(
        "standard",
        "--level",
        "-l",
        help="Compliance level (basic, standard, verified)",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Overwrite existing configuration",
    ),
) -> None:
    """Initialize ethics compliance in your project"""

    config_path = Path(".ai-ethics.yaml")

    # Check if config already exists
    if config_path.exists() and not force:
        console.print(
            "[yellow]Configuration file .ai-ethics.yaml already exists.[/yellow]"
        )
        console.print("Use --force to overwrite.")
        raise typer.Exit(1)

    # Create configuration
    config = {
        "version": "1.0",
        "frameworks": [
            {
                "id": framework,
                "enabled": True,
                "compliance_level": level,
            }
        ],
        "exclude_checks": [],
        "custom_checks": [],
        "metadata": {
            "project_name": Path.cwd().name,
            "last_assessed": None,
            "assessment_tool_version": "0.1.0",
        },
        "reporting": {
            "formats": ["text"],
            "output_dir": "./ethics-reports",
        },
    }

    # Write configuration
    with open(config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    console.print(f"[green]✓[/green] Created .ai-ethics.yaml with {framework} framework")

    # Create docs directory if it doesn't exist
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    # Create template files based on framework
    if framework == "unesco-2021":
        _create_unesco_templates(docs_dir)

    console.print("\n[bold]Next steps:[/bold]")
    console.print("1. Review and customize .ai-ethics.yaml")
    console.print("2. Fill out template files in docs/")
    console.print("3. Run [cyan]ethica check[/cyan] to verify compliance")


def _create_unesco_templates(docs_dir: Path) -> None:
    """Create UNESCO framework template files"""

    # Model card template
    model_card_path = docs_dir / "MODEL_CARD.md"
    if not model_card_path.exists():
        model_card_content = """# Model Card

## Model Details

- **Model Name**: [Your Model Name]
- **Version**: [Version Number]
- **Date**: [Date]
- **Model Type**: [e.g., Neural Network, Random Forest, etc.]
- **Training Data**: [Description of training data]

## Intended Use

- **Primary Use Cases**: [Describe intended applications]
- **Out-of-Scope Uses**: [Describe inappropriate uses]

## Metrics

- **Model Performance**: [Key performance metrics]
- **Decision Thresholds**: [If applicable]

## Training Data

- **Datasets Used**: [List datasets]
- **Preprocessing**: [Data preprocessing steps]
- **Data Splits**: [Train/validation/test split information]

## Ethical Considerations

- **Sensitive Data**: [Any sensitive or personal data used]
- **Bias Considerations**: [Known or potential biases]
- **Limitations**: [Known limitations]

## Recommendations

- **Best Practices**: [Recommendations for responsible use]
- **Monitoring**: [Suggested monitoring approaches]
"""
        model_card_path.write_text(model_card_content)
        console.print(f"[green]✓[/green] Created template: {model_card_path}")

    # Privacy impact assessment template
    privacy_path = docs_dir / "PRIVACY_IMPACT_ASSESSMENT.md"
    if not privacy_path.exists():
        privacy_content = """# Privacy Impact Assessment

## Data Collection

- **What data is collected?**: [Description]
- **How is data collected?**: [Methods]
- **Purpose of collection**: [Justification]

## Data Usage

- **How is data used?**: [Description]
- **Who has access?**: [Access controls]
- **Retention period**: [How long data is kept]

## Data Protection

- **Security measures**: [Technical and organizational measures]
- **Encryption**: [Encryption at rest and in transit]
- **Access controls**: [Who can access what]

## User Rights

- **Right to access**: [How users can access their data]
- **Right to deletion**: [How users can request deletion]
- **Right to rectification**: [How users can correct data]

## Compliance

- **Regulations**: [GDPR, CCPA, etc.]
- **Data Protection Officer**: [Contact information]
- **Last Review**: [Date]
"""
        privacy_path.write_text(privacy_content)
        console.print(f"[green]✓[/green] Created template: {privacy_path}")
