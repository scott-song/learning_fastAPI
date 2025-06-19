# FastAPI Project with Professional Development Setup

A production-ready FastAPI project featuring domain-driven architecture, comprehensive tooling, and automated quality control - optimized for Python 3.12.

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.108+-green.svg)](https://fastapi.tiangolo.com)
[![Poetry](https://img.shields.io/badge/Poetry-dependency%20management-blue.svg)](https://python-poetry.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## 🚀 **Features**

### **Core Framework**

- **FastAPI 0.108+**: Modern, fast web framework with automatic API documentation
- **Domain-Driven Architecture**: Clean separation of concerns with domains (users, items, core)
- **SQLAlchemy 2.0**: Latest ORM with modern async support
- **Alembic**: Database migrations with auto-generation
- **Pydantic v2**: High-performance data validation and serialization

### **Professional Development Tooling**

- **Poetry**: Modern dependency management with lock files
- **Pre-commit Hooks**: Automated code quality checks before commits
- **Comprehensive Linting**: Black, isort, flake8, mypy, bandit
- **Testing Suite**: Pytest with coverage reporting
- **Makefile**: Convenient development shortcuts
- **Type Safety**: Full mypy integration with gradual typing

### **Security & Authentication**

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: bcrypt for secure password storage
- **Security Scanning**: Bandit for vulnerability detection
- **CORS Configuration**: Flexible cross-origin resource sharing

## 📁 **Project Structure**

```
learning_fastAPI/
├── app/                           # Main application
│   ├── main.py                   # FastAPI application entry point
│   ├── api_router.py             # Main API router
│   ├── dependencies.py           # Common dependencies
│   ├── utils.py                  # Utility functions
│   ├── core/                     # Core functionality
│   │   ├── config.py             # Settings and configuration
│   │   └── security.py           # Authentication & security
│   ├── db/                       # Database configuration
│   │   ├── base.py               # Base imports for Alembic
│   │   ├── database.py           # Database connection
│   │   └── init_db.py            # Database initialization
│   ├── crud/                     # Base CRUD operations
│   │   └── base.py               # Generic CRUD class
│   └── domains/                  # Domain-driven modules
│       ├── users/                # User domain
│       │   ├── models/           # User SQLAlchemy models
│       │   ├── schemas/          # User Pydantic schemas
│       │   ├── crud/             # User CRUD operations
│       │   ├── endpoints/        # User API endpoints
│       │   └── service/          # User business logic
│       └── items/                # Item domain
│           ├── models/           # Item models & schemas
│           └── [similar structure]
├── tests/                        # Test suite
│   ├── test_main.py
│   └── api/                      # API tests
├── alembic/                      # Database migrations
│   ├── env.py                    # Alembic configuration
│   ├── versions/                 # Migration files
│   └── script.py.mako
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
├── .flake8                       # Flake8 linting rules
├── .vscode/                      # IDE configuration
├── Makefile                      # Development shortcuts
├── pyproject.toml                # Poetry & tool configuration
├── alembic.ini                   # Alembic settings
├── requirements.txt              # Generated dependencies (for CI/CD)
└── [documentation files]
```

## 🏃‍♂️ **Quick Start**

### **1. Prerequisites**

```bash
# Ensure Python 3.12 is installed
python --version  # Should show Python 3.12.x

# Install Poetry (if not installed)
curl -sSL https://install.python-poetry.org | python3 -
```

### **2. Setup Project**

```bash
# Clone the repository
git clone https://github.com/scott-song/learning_fastAPI.git
cd learning_fastAPI

# Install dependencies
poetry install

# Install pre-commit hooks
make pre-commit-install

# Set up the database
poetry run alembic upgrade head
```

### **3. Run Development Server**

```bash
# Start the development server
make dev

# Or manually:
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### **4. Access the Application**

- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Main Endpoint**: http://localhost:8000

## 🛠️ **Development Workflow**

### **Available Make Commands**

```bash
make help              # Show all available commands
make install           # Install dependencies
make dev              # Start development server

# Code Quality
make format           # Format code with Black
make sort-imports     # Sort imports with isort
make lint             # Run flake8 linting
make type-check       # Run mypy type checking
make check-all        # Run all quality checks

# Testing
make test             # Run tests
make test-cov         # Run tests with coverage

# Pre-commit
make pre-commit-run   # Run all pre-commit hooks
make ci               # Run complete CI pipeline
```

### **Code Quality Pipeline**

Every commit automatically runs:

1. **Black**: Code formatting (79 character lines)
1. **isort**: Import sorting and organization
1. **flake8**: Style guide enforcement and error detection
1. **mypy**: Static type checking
1. **bandit**: Security vulnerability scanning
1. **General checks**: YAML/JSON validation, trailing whitespace, etc.

### **Adding New Features**

#### **1. Create a New Domain**

```bash
mkdir -p app/domains/new_domain/{models,schemas,crud,endpoints,service}
```

#### **2. Add Database Models**

```python
# app/domains/new_domain/models/__init__.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class NewModel(Base):
    __tablename__ = "new_table"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

#### **3. Create Schemas**

```python
# app/domains/new_domain/schemas/__init__.py
from pydantic import BaseModel

class NewModelCreate(BaseModel):
    name: str

class NewModel(NewModelCreate):
    id: int
    class Config:
        from_attributes = True
```

#### **4. Generate Migration**

```bash
poetry run alembic revision --autogenerate -m "Add new_table"
poetry run alembic upgrade head
```

## 🧪 **Testing**

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test file
poetry run pytest tests/test_main.py -v

# Run tests with specific markers
poetry run pytest -m "not slow"
```

## 📊 **Database Management**

### **Migrations**

```bash
# Generate new migration
poetry run alembic revision --autogenerate -m "Description"

# Apply migrations
poetry run alembic upgrade head

# Rollback last migration
poetry run alembic downgrade -1

# View migration history
poetry run alembic history
```

### **Database Schema**

The project includes:

- **Users table**: Authentication and user management
- **Items table**: Sample domain entity with user relationships
- **Alembic version tracking**: Migration history

## 🔧 **Configuration**

### **Environment Variables**

Create a `.env` file (copy from `.env.example`):

```bash
# Database
DATABASE_URL=sqlite:///./app.db

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
```

### **Tool Configuration**

All tools are configured in `pyproject.toml`:

- **Black**: 79-character lines, Python 3.12 target
- **isort**: Black-compatible, organized import sections
- **mypy**: Gradual typing approach
- **pytest**: Coverage reporting, custom markers
- **coverage**: Branch coverage, HTML reports

## 🚀 **Deployment**

### **Production Setup**

```bash
# Install production dependencies only
poetry install --only=main

# Set environment variables
export ENVIRONMENT=production
export DATABASE_URL=postgresql://user:pass@host:port/dbname

# Run with production server
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### **Docker Support**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --only=main
COPY . .
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

## 📚 **Documentation**

- **[Linting Configuration Guide](LINTING_CONFIG.md)**: Comprehensive tool setup
- **[Pre-commit Setup Guide](PRE_COMMIT_SETUP.md)**: Hook configuration and usage
- **[Development Shortcuts](SHORTCUTS.md)**: Makefile commands reference

## 🤝 **Contributing**

1. **Fork the repository**
1. **Create a feature branch**: `git checkout -b feature/amazing-feature`
1. **Make changes** (pre-commit hooks will run automatically)
1. **Run the full CI pipeline**: `make ci`
1. **Commit changes**: `git commit -m "Add amazing feature"`
1. **Push to branch**: `git push origin feature/amazing-feature`
1. **Open a Pull Request**

### **Code Standards**

- **Line length**: 79 characters (Black enforced)
- **Type hints**: Encouraged, gradually enforced by mypy
- **Docstrings**: Google style for public APIs
- **Testing**: Aim for >80% coverage
- **Security**: All code scanned by bandit

## 📈 **Performance & Python 3.12**

This project leverages Python 3.12's improvements:

- **40% faster comprehensions**: Optimized data processing
- **Better error messages**: Enhanced debugging experience
- **Improved asyncio**: Perfect for FastAPI's async capabilities
- **Enhanced type hints**: Better static analysis
- **Per-interpreter GIL**: Future parallelism improvements

## 🆚 **Poetry vs pip/requirements.txt**

| Feature | pip + requirements.txt | Poetry |
|---------|----------------------|--------|
| **Dependency Resolution** | ❌ Manual conflicts | ✅ Automatic resolution |
| **Lock Files** | ❌ No version locking | ✅ `poetry.lock` |
| **Virtual Environments** | ❌ Manual management | ✅ Automatic creation |
| **Dev/Prod Separation** | ❌ Mixed dependencies | ✅ Grouped dependencies |
| **Build System** | ❌ Complex setup.py | ✅ PEP 518 compliant |
| **Publishing** | ❌ Multiple tools | ✅ `poetry publish` |

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- **[FastAPI](https://fastapi.tiangolo.com/)**: Amazing framework by Sebastián Ramírez
- **[Poetry](https://python-poetry.org/)**: Modern dependency management
- **[Pre-commit](https://pre-commit.com/)**: Git hook framework
- **Python 3.12**: Latest performance improvements

______________________________________________________________________

**Built with ❤️ using FastAPI, Poetry, and Python 3.12**
