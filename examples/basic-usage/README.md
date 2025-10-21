# Basic Usage Example

This example demonstrates a minimal AI project with ethics compliance.

## Project Structure

```
basic-usage/
├── README.md                           # This file
├── .ai-ethics.yaml                     # Ethics configuration
├── requirements.txt                    # Project dependencies
├── docs/
│   ├── MODEL_CARD.md                  # Model documentation
│   └── PRIVACY_IMPACT_ASSESSMENT.md   # Privacy documentation
└── src/
    └── model.py                        # Sample model code
```

## Running the Example

From this directory:

```bash
# Install dependencies
pip install -r requirements.txt

# Check compliance
ethica check

# You should see output like:
# Checking against unesco-2021 (standard level)...
#
# Transparency and Explainability ✓
#   ✓ Model Card Documentation: Found docs/MODEL_CARD.md
#   ✓ Explainability Implementation: Found package(s): shap
#
# Fairness and Non-discrimination ✓
#   ✓ Fairness Metrics Library: Found package(s): fairlearn
#
# Privacy and Data Protection ✓
#   ✓ Privacy Impact Assessment: Found docs/PRIVACY_IMPACT_ASSESSMENT.md
#
# Accountability ✓
#   ✓ Version Control: Found .git/
#
# Summary:
# Overall Status: passed
# Pass Rate: 100.0%
# Checks Passed: 5/5
```

## What This Example Shows

1. **Proper documentation**: Model card and privacy assessment
2. **Explainability**: Uses SHAP for model explanations
3. **Fairness**: Includes fairlearn for bias evaluation
4. **Version control**: Git repository
5. **Full compliance**: All checks pass

## Try It Yourself

1. **Modify configuration**:
   ```bash
   # Try different compliance level
   ethica check --level verified
   ```

2. **Remove a dependency**:
   - Comment out `shap` in `requirements.txt`
   - Reinstall: `pip install -r requirements.txt`
   - Re-check: `ethica check`
   - See the warning about missing explainability

3. **Add custom checks**:
   - Edit `.ai-ethics.yaml`
   - Add project-specific requirements under `custom_checks`

## Next Steps

- Review the generated documentation templates
- Explore the UNESCO framework: `ethica frameworks info unesco-2021`
- Try verbose output: `ethica check --verbose`
- Generate JSON report: `ethica check --output json`
