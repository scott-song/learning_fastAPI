# Pre-commit Hooks Setup Guide

This document explains the pre-commit hooks configuration for your Poetry-based FastAPI project.

## 🎯 **What Are Pre-commit Hooks?**

Pre-commit hooks are scripts that run automatically before each git commit to:
- ✅ Validate code quality
- 🔧 Auto-fix formatting issues  
- 🚨 Prevent broken code from being committed
- 📋 Ensure consistent coding standards

## 🛠️ **Installation & Setup**

### **1. Install Pre-commit Hooks**
```bash
make pre-commit-install
# or
poetry run pre-commit install
```

This installs hooks for:
- `pre-commit`: Runs before each commit
- `pre-push`: Runs before each push

### **2. Manual Testing**
```bash
make pre-commit-run
# or  
poetry run pre-commit run --all-files
```

## 📋 **Configured Hooks**

### **🎵 Poetry Hooks** (from [Poetry docs](https://python-poetry.org/docs/pre-commit-hooks/))

| Hook | Description | When It Runs |
|------|-------------|--------------|
| **poetry-check** | Validates `pyproject.toml` structure | Always |
| **poetry-lock** | Ensures `poetry.lock` is up-to-date | When `pyproject.toml` changes |
| **poetry-export** | Updates `requirements.txt` from lock file | When `pyproject.toml` or `poetry.lock` changes |

### **🐍 Python Code Quality Hooks**

| Hook | Description | Auto-fixes |
|------|-------------|------------|
| **Black** | Code formatter | ✅ Yes |
| **isort** | Import sorter | ✅ Yes |
| **Flake8** | Style guide linter | ❌ No |
| **Bandit** | Security linter | ❌ No |

### **📝 General Hooks**

| Hook | Description | Auto-fixes |
|------|-------------|------------|
| **trailing-whitespace** | Removes trailing whitespace | ✅ Yes |
| **end-of-file-fixer** | Ensures files end with newline | ✅ Yes |
| **check-yaml** | Validates YAML syntax | ❌ No |
| **check-json** | Validates JSON syntax | ❌ No |
| **check-toml** | Validates TOML syntax | ❌ No |
| **check-merge-conflict** | Detects merge conflict markers | ❌ No |
| **debug-statements** | Finds debug statements in Python | ❌ No |
| **check-added-large-files** | Prevents large files (>1MB) | ❌ No |

## 🔄 **How Pre-commit Works**

### **Normal Git Workflow**
```bash
# 1. Make changes to your code
git add .

# 2. Commit (pre-commit hooks run automatically)
git commit -m "Your commit message"

# 3. If hooks pass: commit succeeds ✅
# 4. If hooks fail: commit is blocked ❌
```

### **When Hooks Fail**
```bash
# Example: Flake8 finds issues
git commit -m "Add new feature"
# Output: Flake8 Linter...Failed
# - hook id: flake8
# - exit code: 1
# app/new_feature.py:10:1: F401 'os' imported but unused

# Fix the issues, then commit again
git add .
git commit -m "Add new feature"
# Output: All hooks passed! ✅
```

## 🎛️ **Configuration Details**

### **Poetry Hooks Configuration**
```yaml
- repo: https://github.com/python-poetry/poetry
  rev: '1.8.3'
  hooks:
    - id: poetry-check        # Validates pyproject.toml
    - id: poetry-lock         # Checks lock file sync
      args: [--check]
    - id: poetry-export       # Exports requirements.txt
      args: ["-f", "requirements.txt", "-o", "requirements.txt", "--without-hashes"]
```

### **Key Features**
- **poetry-check**: Prevents committing broken `pyproject.toml`
- **poetry-lock**: Ensures dependencies are properly locked
- **poetry-export**: Keeps `requirements.txt` in sync automatically

## 🚀 **Makefile Commands**

| Command | Description |
|---------|-------------|
| `make pre-commit-install` | Install pre-commit hooks |
| `make pre-commit-run` | Run all hooks manually |
| `make pre-commit-update` | Update hooks to latest versions |

## 💡 **Pro Tips**

### **1. Skip Hooks (Emergency Only)**
```bash
# Skip all hooks (use sparingly!)
git commit -m "Emergency fix" --no-verify

# Skip specific hook
SKIP=flake8 git commit -m "WIP: ignore linting for now"
```

### **2. Run Specific Hooks**
```bash
# Run only Poetry hooks
poetry run pre-commit run poetry-check poetry-lock poetry-export

# Run only formatting hooks
poetry run pre-commit run black isort
```

### **3. Update Hook Versions**
```bash
# Update all hooks to latest versions
make pre-commit-update

# Or manually
poetry run pre-commit autoupdate
```

### **4. Performance Optimization**
The configuration includes:
- `fail_fast: false` - Run all hooks even if one fails
- `default_install_hook_types: [pre-commit, pre-push]` - Install both types
- File pattern matching to skip unnecessary runs

## 🔧 **Troubleshooting**

### **Common Issues**

**1. Hook Installation Failed**
```bash
# Reinstall pre-commit
poetry add --group dev pre-commit
make pre-commit-install
```

**2. Poetry Export Fails**
```bash
# Ensure poetry.lock is up to date
poetry lock
poetry run pre-commit run poetry-export
```

**3. Network Issues**
```bash
# Skip problematic hooks temporarily
SKIP=mypy git commit -m "Skip mypy due to network issues"
```

**4. Large Files Blocked**
```bash
# Check file sizes
ls -lh path/to/large/file

# Either reduce file size or exclude it
echo "large_file.dat" >> .gitignore
```

## 📊 **Benefits**

### **Before Pre-commit**
- Manual linting: `make lint`
- Manual formatting: `make format`  
- Inconsistent code quality
- Broken commits slip through

### **After Pre-commit**
- ✅ Automatic code quality checks
- ✅ Consistent formatting
- ✅ Prevents broken commits
- ✅ Team-wide standards enforcement
- ✅ Automatic `requirements.txt` updates

## 🎯 **Integration with CI/CD**

Your pre-commit hooks complement your Makefile workflow:

```bash
# Local development
git commit -m "Feature"  # Pre-commit runs automatically

# CI/CD pipeline  
make ci                  # Runs same checks in CI
```

This ensures the same quality standards locally and in CI! 🚀

## 📋 **Current Status**

Your project now has:
- ✅ Poetry hooks installed and configured
- ✅ Python linting hooks (Black, isort, flake8, bandit)
- ✅ General file quality hooks
- ✅ Automatic `requirements.txt` generation
- ✅ Makefile integration
- ✅ Comprehensive documentation

**Next Steps:**
1. Make a test commit to see hooks in action
2. Share this setup with your team
3. Consider adding more hooks as needed (e.g., commit message validation)

Happy coding! 🎉 