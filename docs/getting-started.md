# Getting Started with Ethica

This guide will walk you through setting up ethics compliance checking for your AI project.

## Installation

### From PyPI (when published)

```bash
pip install ethica
```

### From Source

```bash
git clone https://github.com/shellen/ethica
cd ethica
pip install -e .
```

## Your First Ethics Check

### Step 1: Initialize Your Project

Navigate to your AI project directory and run:

```bash
cd your-ai-project
ethica init
```

This creates:
- `.ai-ethics.yaml` - Configuration file
- `docs/MODEL_CARD.md` - Template for model documentation
- `docs/PRIVACY_IMPACT_ASSESSMENT.md` - Template for privacy documentation

### Step 2: Fill Out Templates

Open the generated templates and fill them out based on your project:

**MODEL_CARD.md** should describe:
- What your model does
- How it was trained
- Known limitations
- Intended use cases

**PRIVACY_IMPACT_ASSESSMENT.md** should document:
- What data you collect
- How you protect it
- User rights and access
- Compliance measures

### Step 3: Run Your First Check

```bash
ethica check
```

You'll see results grouped by ethical principle:

```
Checking against unesco-2021 (standard level)...

Transparency and Explainability ✓
  ✓ Model Card Documentation: Found MODEL_CARD.md
  ✗ Explainability Implementation: No explainability library found
    → Install one of: shap, lime, interpret

...

Summary:
Overall Status: passed with warnings
Pass Rate: 60.0%
Checks Passed: 3/5
```

### Step 4: Address Issues

The check output tells you exactly what's missing. For example:

**Missing explainability library?**
```bash
pip install shap
# Add to requirements.txt
```

**Missing fairness metrics?**
```bash
pip install fairlearn
# Add to requirements.txt
```

### Step 5: Re-check

After making changes:

```bash
ethica check
```

Keep iterating until you reach your target compliance level.

## Understanding Results

### Check Statuses

- **✓ Passed**: Requirement met
- **✗ Failed**: Requirement not met (with suggestion)
- **○ Skipped**: Check not applicable

### Severity Levels

- **Error** (red ✗): Required for compliance
- **Warning** (yellow ✗): Recommended but not required

### Compliance Levels

- **basic** (50% pass rate): Minimum viable compliance
- **standard** (70% pass rate): Industry best practices
- **verified** (95% pass rate): Comprehensive compliance

## Configuring Your Project

Edit `.ai-ethics.yaml` to customize:

```yaml
version: "1.0"

frameworks:
  - id: "unesco-2021"
    enabled: true
    compliance_level: "standard"  # Change to "basic" or "verified"

exclude_checks:
  # Exclude checks that don't apply to your project
  - "unesco-2021/transparency-002"

metadata:
  project_name: "My AI Project"
  team: "AI Ethics Team"
```

## Common Workflows

### Daily Development

```bash
# Quick check during development
ethica check

# Detailed check before committing
ethica check --verbose
```

### Pre-Release

```bash
# Full compliance check
ethica check --level verified

# Generate report for stakeholders
ethica check --output json > compliance-report.json
```

### Exploring Frameworks

```bash
# List available frameworks
ethica frameworks list

# Learn about UNESCO framework
ethica frameworks info unesco-2021
```

## Next Steps

- **Automate checks**: Add to CI/CD pipeline
- **Track progress**: Compare reports over time
- **Share results**: Include in documentation
- **Custom checks**: Add project-specific requirements

## Getting Help

- Check the [README](../README.md) for quick reference
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) to add new checks
- Open an issue on GitHub for bugs or questions
- Review the UNESCO framework in `frameworks/unesco-2021/`

## Tips for Success

1. **Start early**: Initialize ethics checking from day one
2. **Iterate often**: Run checks during development, not just before release
3. **Document thoroughly**: Good documentation helps everyone
4. **Fix errors first**: Focus on required checks (errors) before warnings
5. **Track over time**: Ethics compliance is an ongoing process
