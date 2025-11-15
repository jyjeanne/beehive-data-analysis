# Contributing to Bee Hive Data Analysis

Thank you for your interest in contributing to this project! We welcome contributions from the community, whether they're bug fixes, feature additions, documentation improvements, or new analyses.

## Code of Conduct

Please be respectful and constructive in all interactions. We aim to maintain a welcoming and inclusive community for all contributors.

## How to Contribute

### Reporting Issues

Found a bug or have a suggestion? Please open an issue on GitHub with:

1. **Clear title** describing the problem
2. **Detailed description** of the issue
3. **Steps to reproduce** (if applicable)
4. **Expected vs. actual behavior**
5. **Your environment** (Python version, OS, installed packages)
6. **Screenshots or code snippets** (if relevant)

### Setting Up Your Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/beeDataAnalyze.git
cd beeDataAnalyze

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (including dev tools)
pip install -r requirements.txt

# Install pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install
```

### Making Changes

#### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/add-seasonal-analysis` for new features
- `fix/temperature-calculation-bug` for bug fixes
- `docs/update-methodology` for documentation
- `refactor/improve-data-loading` for refactoring

#### 2. Code Style Guidelines

We follow PEP 8 standards with some additional conventions:

**Python Files:**
- Use Black for code formatting
- Use isort for import organization
- Maximum line length: 100 characters
- Add docstrings to functions and classes

```python
def calculate_heat_loss(u_value, area, delta_t):
    """
    Calculate conductive heat loss using thermal resistance formula.

    Parameters
    ----------
    u_value : float
        Thermal transmittance (W/m²K)
    area : float
        Surface area (m²)
    delta_t : float
        Temperature difference (K)

    Returns
    -------
    float
        Heat loss in Watts
    """
    return u_value * area * delta_t
```

**Jupyter Notebooks:**
- One analysis goal per notebook
- Clear cell organization with markdown sections
- Descriptive cell comments
- Proper data validation
- Export key results and visualizations

#### 3. Commit Messages

Write clear, concise commit messages:

```
# Good
fix: correct temperature calculation in heat loss model
feat: add evaporation loss visualization
docs: update installation instructions

# Avoid
fixes
updated stuff
WIP
```

Format:
- Type: `feat`, `fix`, `docs`, `refactor`, `test`, `style`
- Scope: `(optional)` e.g., `fix(temperature):`
- Subject: Clear, imperative mood, max 50 characters
- Body: Detailed explanation (wrap at 72 characters)

#### 4. Testing

Before submitting:

```bash
# Run code quality checks
black --check .
isort --check-only .
flake8 .

# Format code automatically
black .
isort .

# Run tests (if applicable)
pytest
```

#### 5. Documentation

Update relevant documentation:
- **README.md**: For major feature additions
- **NOTEBOOK_ANALYSIS.txt**: For analysis changes
- **Inline comments**: For complex calculations
- **Docstrings**: For new functions

### Submitting a Pull Request

1. **Push your branch**:
```bash
git push origin feature/your-feature-name
```

2. **Open a Pull Request** with:
   - Clear title describing the change
   - Description of what changed and why
   - Reference to related issues (#123)
   - Screenshots/visualizations for UI changes
   - Test results and verification

3. **PR Template**:
```
## Description
Briefly describe your changes and the motivation behind them.

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (could cause existing functionality to change)
- [ ] Documentation update

## Related Issues
Fixes #(issue number)

## How Has This Been Tested?
Describe your testing approach.

## Verification Checklist
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] No new warnings generated
- [ ] Changes have been tested
- [ ] Code works on Python 3.7+
```

### Large Contributions

For significant changes:

1. **Open an issue first** to discuss your proposal
2. **Discuss the approach** with maintainers
3. **Keep PRs focused** - one feature per PR
4. **Break into smaller commits** for review

## Analysis Contribution Guidelines

### Adding New Analysis

If contributing new analysis or models:

1. **Create a new notebook** or extend existing one:
   - Follow the naming convention: `XyzAnalysis.ipynb`
   - Document assumptions and data requirements
   - Include visualizations
   - Add descriptive markdown cells

2. **Validation**:
   - Verify calculations with test cases
   - Compare with published models where applicable
   - Document limitations

3. **Documentation**:
   - Explain methodology in markdown cells
   - Include formula documentation
   - Reference sources and citations

### Data Contributions

If adding new hive data:

1. **Format**: CSV with headers
2. **Columns**: timestamp, temperature_internal, temperature_external, humidity, etc.
3. **Quality**: Check for missing values and outliers
4. **Documentation**: Include metadata file (collection period, hive type, location, etc.)
5. **Privacy**: Ensure no sensitive personal information

## Development Workflow

### Typical Workflow

```
1. Create issue (optional)
   ↓
2. Create feature branch
   ↓
3. Make changes + commit
   ↓
4. Run tests/checks
   ↓
5. Push and open PR
   ↓
6. Address feedback
   ↓
7. Merge to main
```

### Continuous Improvement

After merge:
- Monitor for issues
- Update documentation if needed
- Consider edge cases
- Share results with community

## Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Credited in release notes
- Acknowledged in project documentation

## Questions?

- Check existing issues and discussions
- Review README.md and documentation
- Open a discussion thread on GitHub
- Contact maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Bee Hive Data Analysis project! 🐝
