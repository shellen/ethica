# Contributing to Ethics AI Commons

Thanks for your interest in contributing! This project aims to make AI ethics compliance accessible to all developers.

## How to Contribute

### Reporting Issues

- Check if the issue already exists
- Provide clear steps to reproduce
- Include version information and environment details
- Describe expected vs actual behavior

### Submitting Code

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/ethica
   cd ethica
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev]"
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

5. **Run Tests and Linting**
   ```bash
   pytest
   black ethics_ai/
   ruff check ethics_ai/
   mypy ethics_ai/
   ```

6. **Commit and Push**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**
   - Reference any related issues
   - Describe what changed and why
   - Ensure CI checks pass

## Development Guidelines

### Code Style

- Use **black** for formatting (line length: 100)
- Follow **PEP 8** conventions
- Use **type hints** for all functions
- Write **docstrings** for public APIs

### Testing

- Write tests for all new features
- Maintain test coverage above 80%
- Use pytest for testing
- Test fixtures go in `tests/fixtures/`

### Documentation

- Update README.md for user-facing changes
- Add docstrings to all public functions
- Include examples in documentation
- Keep documentation concise and practical

## Project Structure

```
ethics_ai/
├── cli/          # CLI commands
├── core/         # Core engine (registry, checker)
├── checks/       # Check implementations
└── utils/        # Utilities

frameworks/       # Framework definitions (YAML)
tests/           # Test suite
docs/            # Documentation
```

## Adding New Checks

To add a new check to the UNESCO framework:

1. **Define the check** in `frameworks/unesco-2021/framework.yaml`:
   ```yaml
   - id: "principle-nnn"
     name: "Check Name"
     principle: "principle-id"
     severity: "error"  # or "warning"
     type: "file-exists"  # or "dependency-check"
     description: "What this checks"
     config:
       # Check-specific config
   ```

2. **Implement if needed** (for custom check types):
   - Create check class in `ethics_ai/checks/`
   - Inherit from `BaseCheck`
   - Implement `run()` method

3. **Add tests** in `tests/unit/test_checks.py`

4. **Update documentation**

## Adding New Frameworks

To add a new ethics framework:

1. **Create framework directory**:
   ```
   frameworks/your-framework-id/
   ├── framework.yaml
   └── checks/
   ```

2. **Define framework** in `framework.yaml` (see UNESCO as example)

3. **Register framework** in `frameworks/registry.yaml`

4. **Add tests** for the new framework

5. **Document** the framework

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Assume good intentions

## Questions?

- Open an issue for discussion
- Check existing issues and PRs
- Review the README and documentation

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.
