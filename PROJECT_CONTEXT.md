# Project Context & Understanding Guide

This document helps maintain context about the project for future development sessions.

## 🎯 **Project Vision & Goals**

### **Primary Purpose**
- **What**: Learning FastAPI with professional development practices
- **Why**: Build production-ready API skills with modern tooling
- **Target**: Domain-driven architecture with comprehensive quality control

### **Key Learning Objectives**
- [ ] Master FastAPI framework fundamentals
- [ ] Implement domain-driven design patterns
- [ ] Set up professional development tooling
- [ ] Learn modern Python packaging with Poetry
- [ ] Understand database migrations with Alembic
- [ ] Practice automated code quality (pre-commit hooks)

## 🏗️ **Architecture Decisions**

### **Domain Structure**
```
domains/
├── users/          # User management & authentication
├── items/          # Sample business domain
└── core/           # Shared utilities
```

**Rationale**: Clean separation of concerns, scalable structure

### **Technology Stack**
- **Framework**: FastAPI (async, automatic docs, type safety)
- **Database**: SQLite → PostgreSQL (development → production)
- **ORM**: SQLAlchemy 2.0 (modern async syntax)
- **Migration**: Alembic (automatic schema generation)
- **Auth**: JWT + bcrypt (stateless, secure)
- **Validation**: Pydantic v2 (performance, type safety)

## 🛠️ **Development Setup Choices**

### **Quality Control Pipeline**
1. **Black**: 79-char formatting (fits terminal/GitHub)
2. **isort**: Import organization
3. **flake8**: Style enforcement
4. **mypy**: Gradual typing (strict=false initially)
5. **bandit**: Security scanning
6. **pre-commit**: Automated quality gates

### **Package Management**
- **Poetry**: Modern dependency management
- **pyproject.toml**: Single configuration file
- **Lock files**: Reproducible builds

## 🎯 **Current Status**

### **Completed Features**
- ✅ Project structure with domain architecture
- ✅ Database setup with User/Item models
- ✅ CRUD operations base class
- ✅ API endpoints for users
- ✅ Authentication system structure
- ✅ Comprehensive development tooling
- ✅ Pre-commit hooks automation
- ✅ Documentation and guides

### **Pending/Future Features**
- [ ] Complete authentication endpoints
- [ ] JWT token validation middleware
- [ ] Items CRUD endpoints
- [ ] User-Item relationships
- [ ] API testing suite
- [ ] Environment configuration
- [ ] Production deployment setup
- [ ] API rate limiting
- [ ] Logging and monitoring

## 🚧 **Known Issues & Technical Debt**

### **Type Safety**
- MyPy errors in user CRUD (Column[str] vs str types)
- Need proper SQLAlchemy model type annotations
- Consider using SQLModel for better type integration

### **Configuration**
- Missing .env.example file
- Need environment-specific settings
- Database URL should be configurable

### **Testing**
- Basic test structure exists but needs expansion
- Need integration tests for API endpoints
- Database testing with fixtures needed

## 📋 **Development Patterns**

### **Adding New Domains**
1. Create domain directory: `app/domains/new_domain/`
2. Add models, schemas, crud, endpoints, service
3. Generate migration: `alembic revision --autogenerate`
4. Update API router in `api_router.py`
5. Add tests in `tests/api/`

### **Code Quality Workflow**
1. Write code
2. Run `make check-all` locally
3. Commit (pre-commit hooks run automatically)
4. Push (pre-push hooks validate)

### **Database Changes**
1. Modify SQLAlchemy models
2. Generate migration: `alembic revision --autogenerate`
3. Review migration file
4. Apply: `alembic upgrade head`

## 💡 **Future Improvements**

### **Short Term**
- Fix type safety issues
- Add comprehensive test suite
- Complete authentication flow
- Add API documentation examples

### **Medium Term**
- Add caching (Redis)
- Implement API versioning
- Add background tasks (Celery)
- Set up CI/CD pipeline

### **Long Term**
- Microservice architecture
- Event-driven patterns
- Performance optimization
- Production monitoring

## 🎓 **Learning Resources Used**

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Domain-Driven Design Patterns](https://martinfowler.com/bliki/DomainDrivenDesign.html)

## 📞 **Questions for Future Sessions**

**Always ask about:**
1. What specific feature/domain are we working on?
2. Are we adding new functionality or refactoring existing?
3. Should we maintain the current architecture patterns?
4. Any specific performance or security requirements?
5. Testing approach for new features?

**Context to remember:**
- This is a learning project focused on best practices
- Code quality and documentation are prioritized
- Domain-driven architecture should be maintained
- All changes should include proper tests
- Security and performance are important considerations
