# Development Shortcuts - Makefile

This FastAPI project uses **Makefile** for convenient development shortcuts.

## 🚀 **Quick Start**

```bash
make help           # Show all available commands
make check-all      # Run all code quality checks
make dev            # Start development server
```

## 📋 **Available Commands**

| Command | Description | Equivalent |
|---------|-------------|------------|
| `make help` | Show this help message | - |
| `make install` | Install dependencies | `poetry install` |
| `make format` | Format code with Black | `poetry run black app/ tests/` |
| `make sort-imports` | Sort imports with isort | `poetry run isort app/ tests/` |
| `make lint` | Run flake8 linting | `poetry run flake8 app/ tests/` |
| `make type-check` | Run mypy type checking | `poetry run mypy app/` |
| `make test` | Run tests | `poetry run pytest` |
| `make test-cov` | Run tests with coverage | `poetry run pytest --cov=app --cov-report=html` |
| `make dev` | Start development server | `poetry run uvicorn app.main:app --reload` |
| `make clean` | Clean cache and temporary files | Remove __pycache__, .pyc files |
| `make check-all` | Run all quality checks | format + sort-imports + lint + type-check |
| `make ci` | Run full CI pipeline | check-all + test |

## 🔄 **Common Workflows**

### Before Committing Code:
```bash
make check-all      # Format, sort imports, lint, type-check
```

### Full CI Check:
```bash
make ci             # All quality checks + tests
```

### Development Server:
```bash
make dev            # Start with auto-reload
```

### After Git Pull:
```bash
make install        # Update dependencies
make clean          # Clear cache
```

## 💡 **Pro Tips**

1. **Always run `make check-all`** before committing
2. **Use `make ci`** to simulate the full CI pipeline locally
3. **Run `make clean`** if you encounter import or cache issues
4. **Use `make dev`** for development with auto-reload
5. **Tab completion works** - type `make` + TAB to see options

## ✅ **Benefits of Makefile**

- **Universal** - Works on macOS, Linux, and Windows (with make installed)
- **Fast** - No Python startup overhead
- **Standard** - Industry-standard approach used by most projects
- **Simple** - Easy to understand and modify
- **Reliable** - Consistent across team members and CI/CD

## 🎯 **Your New Workflow**

Instead of typing:
```bash
poetry run black app/ tests/
poetry run isort app/ tests/
poetry run flake8 app/ tests/
poetry run mypy app/
```

Just type:
```bash
make check-all
```

**That's it!** 🎉 Your development workflow is now streamlined and professional.
