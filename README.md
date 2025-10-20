# Ethics AI Commons

**Framework-agnostic platform for AI ethics compliance checking**

Think "ESLint for AI Ethics" - pluggable frameworks, automated checks, CI/CD integration, and actionable guidance.

## Why Use This?

Building ethical AI shouldn't require a PhD in ethics or months of manual audits. Ethics AI Commons:

- **Automates compliance checking** against global standards like UNESCO's AI Ethics Recommendation
- **Catches issues early** in development, not after deployment
- **Provides clear guidance** on what's missing and how to fix it
- **Integrates into your workflow** via CLI, CI/CD, and git hooks
- **Works with any framework** - use existing standards or define your own

## Quick Start

```bash
# Install (when published)
pip install ethics-ai-commons

# Or install from source
git clone https://github.com/shellen/ethica
cd ethica
pip install -e .

# Initialize in your AI project
cd your-ai-project
ethics-ai init

✓ Created .ai-ethics.yaml with unesco-2021 framework
✓ Created template files in docs/
  - MODEL_CARD.md
  - PRIVACY_IMPACT_ASSESSMENT.md

# Check compliance
ethics-ai check

Checking against unesco-2021 (standard level)...

Transparency and Explainability ✗
  ✓ Model Card Documentation: Found MODEL_CARD.md
  ✗ Explainability Implementation: No explainability library found
    → Install one of: shap, lime, interpret

Fairness and Non-discrimination ✗
  ✗ Fairness Metrics Library: No fairness evaluation tools found
    → Install one of: fairlearn, aif360, themis-ml

Privacy and Data Protection ✓
  ✓ Privacy Impact Assessment: Found PRIVACY_IMPACT_ASSESSMENT.md

Accountability ✓
  ✓ Version Control: Found .git/

Summary:
Overall Status: passed with warnings
Pass Rate: 60.0%
Checks Passed: 3/5

# List available frameworks
ethics-ai frameworks list

Available Ethics Frameworks
┌──────────────┬─────────────────────────────────────────┬─────────┬──────────┐
│ ID           │ Name                                    │ Version │ Category │
├──────────────┼─────────────────────────────────────────┼─────────┼──────────┤
│ unesco-2021  │ UNESCO AI Ethics Recommendation 2021    │ 1.0.0   │ intl.    │
└──────────────┴─────────────────────────────────────────┴─────────┴──────────┘
```

## Features

- 🌍 **Global Standards**: Built-in support for UNESCO AI Ethics Recommendation 2021
- 🔌 **Framework Agnostic**: Use existing frameworks or create your own
- ⚡ **Fast**: Runs in seconds on typical projects
- 🤖 **CI/CD Ready**: GitHub Actions and pre-commit hooks included
- 📊 **Clear Reporting**: Actionable feedback on ethics compliance

## What It Checks

### Transparency & Explainability
- Model card documentation
- Explainability implementation
- Decision logging

### Fairness & Non-discrimination
- Bias testing frameworks
- Fairness metrics

### Privacy & Data Protection
- Privacy impact assessments
- PII detection

### Accountability
- Version control
- Audit logging

### Safety & Security
- Security testing frameworks
- Error handling

## Usage Examples

### Basic Usage

```bash
# Initialize with default settings (UNESCO framework, standard level)
ethics-ai init

# Check compliance
ethics-ai check

# Check with verbose output (shows all checks, including passing ones)
ethics-ai check --verbose

# Output results as JSON
ethics-ai check --output json > ethics-report.json
```

### Using Different Compliance Levels

The UNESCO framework supports three compliance levels:

- **basic**: Minimum requirements (50% pass rate, core principles only)
- **standard**: Comprehensive coverage (70% pass rate, most principles) - *default*
- **verified**: Full compliance (95% pass rate, all principles)

```bash
# Initialize with basic level
ethics-ai init --level basic

# Override level when checking
ethics-ai check --level verified
```

### Framework Information

```bash
# List all available frameworks
ethics-ai frameworks list

# Get detailed info about a framework
ethics-ai frameworks info unesco-2021
```

### Configuration File

The `.ai-ethics.yaml` file controls your project's ethics compliance:

```yaml
version: "1.0"

frameworks:
  - id: "unesco-2021"
    enabled: true
    compliance_level: "standard"

exclude_checks:
  # Optionally exclude specific checks
  - "unesco-2021/transparency-002"

metadata:
  project_name: "My AI Project"
  team: "AI Ethics Team"
```

## Development

```bash
# Clone repository
git clone https://github.com/shellen/ethica
cd ethica

# Setup development environment
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black ethics_ai/
ruff check ethics_ai/
```

## Roadmap

**Current (v0.1 - Minimal Viable Product)**
- ✅ UNESCO 2021 framework with 5 core checks
- ✅ CLI tool (init, check, frameworks commands)
- ✅ File-exists and dependency-check types
- ✅ Terminal output with clear guidance

**Planned (v0.2)**
- GitHub Action for CI/CD integration
- Pre-commit hooks
- Additional check types (code-pattern, custom-script)
- More UNESCO checks (10+ total)

**Future (v1.0+)**
- Additional frameworks (IEEE, EU AI Act, NIST)
- Badge generation
- HTML report generation
- MCP server for real-time guidance

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.

## Attribution

This tool implements the UNESCO AI Ethics Recommendation (2021) but is not officially endorsed by UNESCO.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
