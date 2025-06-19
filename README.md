# FastAPI Project Structure

This project follows FastAPI best practices for a scalable and maintainable API structure, optimized for Python 3.12.

## Requirements

- **Python 3.12+** (This project is optimized for Python 3.12's performance improvements)
- pip or poetry for package management

## Project Structure

```
learning_fastAPI/
├── app/                    # Main application directory
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── dependencies.py    # Common dependencies
│   ├── utils.py          # Utility functions
│   ├── api/              # API routes
│   │   ├── __init__.py
│   │   └── v1/           # API version 1
│   │       ├── __init__.py
│   │       ├── api.py    # Main API router
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── users.py
│   │           └── items.py
│   ├── core/             # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py     # Configuration settings
│   │   └── security.py   # Security utilities
│   ├── crud/             # CRUD operations
│   │   ├── __init__.py
│   │   ├── base.py       # Base CRUD class
│   │   ├── crud_user.py  # User CRUD operations
│   │   └── crud_item.py  # Item CRUD operations
│   ├── db/               # Database related
│   │   ├── __init__.py
│   │   ├── database.py   # Database connection
│   │   ├── models.py     # SQLAlchemy models
│   │   ├── base.py       # Base imports for Alembic
│   │   └── init_db.py    # Database initialization
│   └── schemas/          # Pydantic models/schemas
│       ├── __init__.py
│       ├── user.py       # User schemas
│       └── item.py       # Item schemas
├── alembic/              # Database migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── tests/                # Test directory
│   ├── __init__.py
│   ├── test_main.py
│   └── api/
│       ├── __init__.py
│       └── test_*.py
├── requirements.txt      # Python dependencies
├── pyproject.toml       # Project configuration and Python 3.12 settings
├── runtime.txt          # Python version for deployment
├── alembic.ini          # Alembic configuration
└── README.md            # This file
```

## Quick Start

1. **Ensure Python 3.12 is installed:**
   ```bash
   python --version  # Should show Python 3.12.x
   ```

2. **Install Poetry (if not installed):**
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Activate virtual environment:**
   ```bash
   poetry shell
   ```

5. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

6. **Initialize the database:**
   ```bash
   poetry run alembic upgrade head
   ```

7. **Run the development server:**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

6. **Visit the API documentation:**
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## Python 3.12 Features & Benefits

This project leverages Python 3.12's improvements:

- **40% faster comprehensions** - Improved performance for data processing
- **Better error messages** - More precise debugging information
- **Enhanced type hints** - Better static analysis support
- **Improved asyncio performance** - Perfect for FastAPI's async capabilities
- **Per-interpreter GIL** - Future-proofing for better parallelism

## Why Poetry over requirements.txt?

| Feature | requirements.txt | Poetry |
|---------|-----------------|--------|
| **Dependency Resolution** | ❌ Manual conflicts | ✅ Automatic resolution |
| **Lock Files** | ❌ No version locking | ✅ poetry.lock file |
| **Virtual Environments** | ❌ Manual management | ✅ Automatic creation |
| **Dev/Prod Separation** | ❌ Mixed dependencies | ✅ Grouped dependencies |
| **Version Updates** | ❌ Manual editing | ✅ `poetry update` |
| **Package Publishing** | ❌ Complex setup | ✅ `poetry publish` |
| **Dependency Tree** | ❌ No visualization | ✅ `poetry show --tree` |

**Migration Note:** `requirements.txt` is kept for compatibility, but Poetry is the recommended approach.

## Features

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy 2.0**: Latest SQL toolkit and ORM with modern syntax
- **Alembic**: Database migration tool
- **Pydantic v2**: High-performance data validation using Python type hints
- **Authentication**: JWT-based authentication with bcrypt password hashing
- **CORS**: Configurable CORS middleware
- **Environment-based configuration**: Using Pydantic BaseSettings
- **Testing**: Pytest setup with test client
- **Code organization**: Modular structure following FastAPI best practices

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Quality (Python 3.12 optimized)
```bash
# Format code with Black (Python 3.12 target)
poetry run black app/ tests/

# Sort imports
poetry run isort app/ tests/

# Type checking with mypy (Python 3.12)
poetry run mypy app/

# Run all quality checks
poetry run pre-commit run --all-files
```

### Dependency Management
```bash
# Add a new dependency
poetry add requests

# Add a development dependency
poetry add --group dev pytest-mock

# Update all dependencies
poetry update

# Show dependency tree
poetry show --tree

# Export to requirements.txt (for CI/CD compatibility)
poetry export -f requirements.txt --output requirements.txt
```

### Database Migrations
```bash
# Create a new migration
poetry run alembic revision --autogenerate -m "Description of changes"

# Apply migrations
poetry run alembic upgrade head

# Rollback migrations
poetry run alembic downgrade -1
```

### Adding New Endpoints

1. Create new endpoint in `app/api/v1/endpoints/`
2. Add the router to `app/api/v1/api.py`
3. Create corresponding schemas in `app/schemas/`
4. Add CRUD operations in `app/crud/`
5. Update database models in `app/db/models.py` if needed

## Configuration

The application uses environment variables for configuration. Create a `.env` file with:

```env
# Application
PROJECT_NAME="FastAPI Project"
VERSION="1.0.0"
API_V1_STR="/api/v1"

# Database
DATABASE_URL="sqlite:///./app.db"

# Security
SECRET_KEY="your-secret-key-here-change-in-production"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
BACKEND_CORS_ORIGINS="http://localhost,http://localhost:3000"
```

## Deployment

This project is ready for deployment on:
- **Heroku** (runtime.txt specifies Python 3.12)
- **Docker** (Python 3.12 base image)
- **AWS Lambda** (Python 3.12 runtime)
- **Railway**, **Render**, etc.

## Performance Notes

With Python 3.12, you can expect:
- Faster API response times (up to 10-15% improvement)
- Better memory usage for large datasets
- Improved async/await performance for concurrent requests
- Enhanced debugging capabilities during development
