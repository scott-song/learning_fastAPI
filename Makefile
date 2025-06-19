.PHONY: help format sort-imports lint type-check test test-cov dev clean check-all install format-md check-md

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies
	poetry install

format:  ## Format code with Black and markdown
	poetry run black app/ tests/
	poetry run mdformat *.md

sort-imports:  ## Sort imports with isort
	poetry run isort app/ tests/

lint:  ## Run flake8 linting
	poetry run flake8 app/ tests/

type-check:  ## Run mypy type checking
	poetry run mypy app/

test:  ## Run tests
	poetry run pytest

test-cov:  ## Run tests with coverage
	poetry run pytest --cov=app --cov-report=html --cov-report=term

dev:  ## Start development server
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

clean:  ## Clean cache and temporary files
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

format-md:  ## Format markdown files
	poetry run mdformat *.md

check-md:  ## Check markdown formatting
	poetry run mdformat --check *.md

check-all: format sort-imports lint type-check check-md  ## Run all code quality checks

ci: check-all test  ## Run all CI checks (format, lint, type-check, test)

# Pre-commit hooks
pre-commit-install:  ## Install pre-commit hooks
	poetry run pre-commit install

pre-commit-run:  ## Run all pre-commit hooks
	poetry run pre-commit run --all-files

pre-commit-update:  ## Update pre-commit hooks to latest versions
	poetry run pre-commit autoupdate
