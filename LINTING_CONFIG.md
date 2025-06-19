# Linting Tool Configuration Guide

This guide explains how to configure linting tools in a Poetry-based FastAPI project.

## 🎯 **Configuration Files**

| Tool | Configuration File | Location |
|------|-------------------|----------|
| **Black** | `pyproject.toml` | `[tool.black]` |
| **isort** | `pyproject.toml` | `[tool.isort]` |
| **mypy** | `pyproject.toml` | `[tool.mypy]` |
| **flake8** | `.flake8` | Root directory |
| **pytest** | `pyproject.toml` | `[tool.pytest.ini_options]` |
| **coverage** | `pyproject.toml` | `[tool.coverage.*]` |

## 🖤 **Black Configuration**

```toml
[tool.black]
line-length = 79                   # Max line length
target-version = ['py312']         # Target Python version
include = '\.pyi?$'                # Include Python files
extend-exclude = '''
/(
    \.git
  | \.mypy_cache
  | \.pytest_cache
  | \.venv
  | migrations
)/
'''
```

### **Common Black Options:**
- `line-length`: Maximum line length (default: 88)
- `target-version`: Python versions to target
- `include`: File patterns to include
- `extend-exclude`: Additional patterns to exclude
- `force-exclude`: Force exclusion even if files are passed explicitly
- `preview`: Enable preview features

## 📦 **isort Configuration**

```toml
[tool.isort]
profile = "black"                  # Compatible with Black
line_length = 79                   # Match Black's line length
multi_line_output = 3              # Vertical hanging indent
include_trailing_comma = true      # Add trailing comma
force_grid_wrap = 0                # Don't force grid wrap
use_parentheses = true             # Use parentheses for line continuation
sections = [
    "FUTURE",
    "STDLIB",
    "THIRDPARTY",
    "FIRSTPARTY",
    "LOCALFOLDER"
]
known_first_party = ["app"]        # Your app modules
known_third_party = [
    "fastapi",
    "pydantic",
    "sqlalchemy"
]
```

### **Common isort Options:**
- `profile`: Predefined configuration (black, django, pycharm, etc.)
- `multi_line_output`: How to handle multi-line imports (0-5)
- `line_length`: Maximum line length
- `known_first_party`: Your own modules
- `known_third_party`: Third-party modules
- `sections`: Order of import sections
- `force_single_line`: Force single line imports
- `combine_as_imports`: Combine `from` imports

## 🔍 **MyPy Configuration**

```toml
[tool.mypy]
python_version = "3.12"
strict = false                     # Start less strict
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = true      # Ignore missing stubs
show_error_codes = true            # Show error codes
pretty = true                      # Pretty output

# Gradually enable these
disallow_untyped_defs = false      # Allow untyped functions
disallow_incomplete_defs = false   # Allow incomplete definitions
no_implicit_optional = false       # Allow implicit Optional

exclude = [
    "migrations/",
    "tests/",
    "alembic/"
]

# Per-module options
[[tool.mypy.overrides]]
module = "tests.*"
ignore_errors = true
```

### **MyPy Strictness Levels:**
1. **Beginner** (current): `strict = false`, allow untyped code
2. **Intermediate**: Enable `disallow_untyped_defs = true`
3. **Advanced**: Enable `strict = true`
4. **Expert**: Add `disallow_any_generics = true`

### **Common MyPy Options:**
- `strict`: Enable all strict checks
- `disallow_untyped_defs`: Require type annotations for functions
- `disallow_any_generics`: Disallow `Any` in generic types
- `warn_return_any`: Warn when returning `Any`
- `ignore_missing_imports`: Ignore missing type stubs
- `show_error_codes`: Show error codes in output

## 🚨 **Flake8 Configuration**

```ini
[flake8]
max-line-length = 79
max-complexity = 10
select = E,W,F,C
ignore = E203,W503,W504
exclude =
    .git,
    __pycache__,
    .venv,
    migrations,
    alembic
per-file-ignores =
    __init__.py:F401,F403
    test_*.py:F841
```

### **Common Flake8 Options:**
- `max-line-length`: Maximum line length
- `max-complexity`: Maximum cyclomatic complexity
- `select`: Error codes to check (E=errors, W=warnings, F=pyflakes, C=complexity)
- `ignore`: Error codes to ignore
- `exclude`: Files/directories to exclude
- `per-file-ignores`: Ignore specific codes for specific files

### **Useful Flake8 Error Codes:**
- `E203`: Whitespace before ':' (conflicts with Black)
- `W503`: Line break before binary operator
- `F401`: Module imported but unused
- `F841`: Local variable assigned but never used
- `C901`: Function is too complex

## 🧪 **Pytest Configuration**

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = [
    "-v",                           # Verbose
    "--tb=short",                   # Short traceback
    "--cov=app",                    # Coverage
    "--cov-fail-under=80",          # Minimum coverage
    "--strict-markers",             # Strict markers
]
markers = [
    "slow: marks tests as slow",
    "integration: integration tests",
    "unit: unit tests",
]
```

### **Common Pytest Options:**
- `testpaths`: Directories to search for tests
- `python_files`: Test file patterns
- `python_classes`: Test class patterns
- `addopts`: Default command-line options
- `markers`: Custom test markers

## 📊 **Coverage Configuration**

```toml
[tool.coverage.run]
source = ["app"]
omit = [
    "*/tests/*",
    "*/migrations/*",
    "app/db/init_db.py",
]
branch = true                      # Branch coverage

[tool.coverage.report]
precision = 2                      # Decimal precision
show_missing = true               # Show missing lines
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
]
```

### **Coverage Options:**
- `source`: Directories to measure
- `omit`: Files to exclude
- `branch`: Enable branch coverage
- `precision`: Decimal places in percentages
- `show_missing`: Show line numbers of missing coverage

## 🎛️ **Customization Examples**

### **Stricter MyPy (Gradual Adoption)**
```toml
[tool.mypy]
strict = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
no_implicit_optional = true
```

### **Relaxed Flake8 for Legacy Code**
```ini
[flake8]
max-line-length = 120
max-complexity = 15
ignore = E203,W503,W504,F401,E501
```

### **Black with Longer Lines**
```toml
[tool.black]
line-length = 88
skip-string-normalization = true
```

## 🔄 **Testing Configuration Changes**

```bash
# Test individual tools
make format          # Test Black
make sort-imports    # Test isort
make lint            # Test flake8
make type-check      # Test mypy

# Test all together
make check-all       # All quality checks
```

## 💡 **Pro Tips**

1. **Start Less Strict**: Begin with relaxed settings, gradually tighten
2. **Tool Compatibility**: Ensure Black, isort, and flake8 work together
3. **Per-File Ignores**: Use for legacy code or special cases
4. **CI Integration**: Use same settings in CI/CD pipelines
5. **Team Consensus**: Agree on rules with your team

## 🎯 **Recommended Progression**

### **Phase 1: Basic Setup**
- Configure Black and isort
- Basic flake8 rules
- MyPy with `strict = false`

### **Phase 2: Intermediate**
- Enable more MyPy warnings
- Add coverage requirements
- Stricter flake8 rules

### **Phase 3: Advanced**
- MyPy strict mode
- High coverage requirements (90%+)
- Custom flake8 plugins

## 🚀 **Your Current Setup**

Your project is configured for **Phase 1** with room to grow:
- ✅ Black + isort compatibility
- ✅ Reasonable flake8 rules
- ✅ MyPy with gradual typing
- ✅ Good test coverage setup
- ✅ Makefile integration

You can gradually tighten the rules as your codebase matures! 🎉
