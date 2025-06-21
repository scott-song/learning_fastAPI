# 🔍 **FastAPI Dependency Injection Deep Dive**

Understanding how `Depends(get_db)` works under the hood - from Python introspection to production patterns.

## 📋 **Table of Contents**

1. [Core Concepts](#core-concepts)
1. [How FastAPI Resolves Dependencies](#how-fastapi-resolves-dependencies)
1. [Real Implementation Examples](#real-implementation-examples)
1. [Advanced Patterns](#advanced-patterns)
1. [Performance Considerations](#performance-considerations)
1. [Best Practices](#best-practices)

______________________________________________________________________

## 🎯 **Core Concepts**

### **What is Dependency Injection?**

Dependency Injection (DI) is a design pattern where objects receive their dependencies from external sources rather than creating them internally. FastAPI's DI system automatically resolves and injects these dependencies into your endpoint functions.

### **The Magic Behind `Depends()`**

```python
# When you write this:
@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return user_crud.get_multi(db)

# FastAPI internally:
# 1. Inspects the function signature using Python's `inspect` module
# 2. Finds parameters with `Depends()` objects
# 3. Executes dependency functions in the correct order
# 4. Injects resolved values as function arguments
# 5. Calls your endpoint with all dependencies resolved
```

______________________________________________________________________

## 🔧 **How FastAPI Resolves Dependencies**

### **Step-by-Step Process**

```python
import inspect
from typing import get_type_hints

# 1. Function Signature Inspection
def analyze_endpoint(func):
    signature = inspect.signature(func)
    type_hints = get_type_hints(func)

    dependencies = {}
    for param_name, param in signature.parameters.items():
        if isinstance(param.default, Depends):
            dependencies[param_name] = {
                'dependency_func': param.default.dependency,
                'type_hint': type_hints.get(param_name),
                'use_cache': param.default.use_cache
            }

    return dependencies

# 2. Dependency Graph Resolution
class DependencyGraph:
    def __init__(self):
        self.resolved = {}
        self.resolving = set()  # Prevent circular dependencies

    def resolve(self, dependency_func):
        # Check for circular dependencies
        if dependency_func in self.resolving:
            raise CircularDependencyError()

        # Check cache
        if dependency_func in self.resolved:
            return self.resolved[dependency_func]

        self.resolving.add(dependency_func)

        # Resolve sub-dependencies first
        sub_deps = analyze_endpoint(dependency_func)
        resolved_sub_deps = {}

        for name, dep_info in sub_deps.items():
            resolved_sub_deps[name] = self.resolve(dep_info['dependency_func'])

        # Execute dependency with resolved sub-dependencies
        result = dependency_func(**resolved_sub_deps)

        self.resolving.remove(dependency_func)
        self.resolved[dependency_func] = result

        return result
```

### **Generator Dependencies (like `get_db`)**

```python
def get_db():
    db = SessionLocal()
    try:
        yield db  # 👈 This is where FastAPI gets the value
    finally:
        db.close()  # 👈 This runs after the endpoint completes

# FastAPI handles generators specially:
# 1. Calls next() to get the yielded value
# 2. Stores the generator for later cleanup
# 3. After endpoint completes, calls generator.close()
# 4. This triggers the finally block for cleanup
```

______________________________________________________________________

## 🏭 **Real Implementation Examples**

### **Your Project's `get_db` Function**

```python
# From app/db/database.py
from sqlalchemy.orm import sessionmaker, Session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Database session dependency"""
    db = SessionLocal()  # Create new session
    try:
        yield db  # Provide session to endpoint
    finally:
        db.close()  # Always cleanup, even on exceptions
```

### **How It's Used in Endpoints**

```python
# From app/domains/users/endpoints/__init__.py
@router.get("/", response_model=List[User])
def read_users(
    skip: int = 0,           # Query parameter
    limit: int = 100,        # Query parameter
    db: Session = Depends(get_db)  # Injected dependency
):
    """FastAPI automatically:
    1. Extracts skip/limit from query params
    2. Calls get_db() to create database session
    3. Passes both to read_users()
    4. After endpoint returns, triggers db.close()
    """
    users = user_crud.get_multi(db, skip=skip, limit=limit)
    return users
```

### **Nested Dependencies**

```python
# Dependencies can depend on other dependencies!

def get_db():
    """Level 1: Database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db)):
    """Level 2: Depends on database"""
    # Get user from database using the injected session
    return user_crud.get_current_user(db)

def get_current_active_user(
    current_user: User = Depends(get_current_user)
):
    """Level 3: Depends on current user"""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@router.get("/profile")
def read_own_profile(
    current_user: User = Depends(get_current_active_user)
):
    """FastAPI resolves the entire chain:
    get_db() → get_current_user() → get_current_active_user() → endpoint
    """
    return current_user
```

______________________________________________________________________

## 🚀 **Advanced Patterns**

### **Dependency Caching**

```python
# FastAPI caches dependencies within a single request
def expensive_computation():
    print("This only runs once per request!")
    return perform_heavy_calculation()

@router.get("/endpoint1")
def endpoint1(result = Depends(expensive_computation)):
    return {"data": result}

@router.get("/endpoint2")
def endpoint2(result = Depends(expensive_computation)):
    # Same computation, but cached result is reused
    return {"processed": result}

# To disable caching:
@router.get("/always-fresh")
def always_fresh(result = Depends(expensive_computation, use_cache=False)):
    return {"fresh": result}
```

### **Sub-Dependencies**

```python
# Dependencies can have their own dependencies
def get_redis_client():
    return redis.Redis(host='localhost', port=6379)

def get_cache_service(redis_client = Depends(get_redis_client)):
    return CacheService(redis_client)

def get_user_service(
    db: Session = Depends(get_db),
    cache: CacheService = Depends(get_cache_service)
):
    return UserService(db, cache)

@router.get("/users/{user_id}")
def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    """FastAPI resolves entire dependency tree:
    get_redis_client() → get_cache_service() ↘
                                              → get_user_service() → endpoint
    get_db() ────────────────────────────────↗
    """
    return user_service.get_by_id(user_id)
```

### **Class-Based Dependencies**

```python
class DatabaseManager:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

@router.get("/users/{user_id}")
def get_user(
    user_id: int,
    db_manager: DatabaseManager = Depends(DatabaseManager)
):
    """FastAPI can instantiate classes as dependencies"""
    return db_manager.get_user(user_id)
```

______________________________________________________________________

## ⚡ **Performance Considerations**

### **Connection Pool Management**

```python
# Your database setup (app/db/database.py)
engine = create_engine(
    str(settings.DATABASE_URL),
    connect_args={"check_same_thread": False},
    pool_size=20,        # Connection pool size
    max_overflow=30,     # Additional connections beyond pool_size
    pool_pre_ping=True,  # Validate connections before use
    pool_recycle=3600    # Recycle connections every hour
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Each request gets its own session from the pool"""
    db = SessionLocal()  # Gets connection from pool
    try:
        yield db
    finally:
        db.close()  # Returns connection to pool (doesn't close it!)
```

### **Dependency Resolution Timing**

```python
# FastAPI resolves dependencies in this order:
@router.post("/users")
def create_user(
    user_data: UserCreate,                    # 1. Request body parsing
    skip: int = Query(0),                     # 2. Query parameters
    db: Session = Depends(get_db),            # 3. Dependencies (in order)
    current_user: User = Depends(get_current_user),  # 4. Sub-dependencies
):
    # 5. Finally, your endpoint code runs
    return user_crud.create(db, obj_in=user_data)
```

______________________________________________________________________

## 🎯 **Best Practices**

### **1. Keep Dependencies Pure**

```python
# ✅ Good: Pure dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ❌ Bad: Side effects in dependency
def get_db_with_logging():
    print("Creating database session")  # Side effect!
    db = SessionLocal()
    try:
        yield db
    finally:
        print("Closing database session")  # More side effects!
        db.close()
```

### **2. Use Type Hints**

```python
# ✅ Good: Clear type hints
def get_user_service(
    db: Session = Depends(get_db)
) -> UserService:
    return UserService(db)

# ❌ Bad: No type hints
def get_user_service(db = Depends(get_db)):
    return UserService(db)
```

### **3. Handle Errors Gracefully**

```python
# ✅ Good: Proper error handling
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = user_crud.get(db, id=user_id)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### **4. Optimize Database Sessions**

```python
# ✅ Good: One session per request
@router.get("/user-with-items/{user_id}")
def get_user_with_items(
    user_id: int,
    db: Session = Depends(get_db)  # Single session for entire request
):
    user = user_crud.get(db, id=user_id)
    items = item_crud.get_by_owner(db, owner_id=user_id)
    return {"user": user, "items": items}

# ❌ Bad: Multiple sessions
@router.get("/user-with-items/{user_id}")
def get_user_with_items_bad(
    user_id: int,
    user_db: Session = Depends(get_db),
    item_db: Session = Depends(get_db)  # Unnecessary second session
):
    user = user_crud.get(user_db, id=user_id)
    items = item_crud.get_by_owner(item_db, owner_id=user_id)
    return {"user": user, "items": items}
```

______________________________________________________________________

## 🔍 **Debugging Dependencies**

### **Inspect Dependency Resolution**

```python
import inspect
from fastapi import Depends

def debug_dependencies(func):
    """Helper to understand dependency resolution"""
    signature = inspect.signature(func)

    print(f"Function: {func.__name__}")
    for param_name, param in signature.parameters.items():
        if isinstance(param.default, Depends):
            dep_func = param.default.dependency
            print(f"  {param_name}: {dep_func.__name__}()")

            # Check if dependency has sub-dependencies
            sub_signature = inspect.signature(dep_func)
            for sub_param_name, sub_param in sub_signature.parameters.items():
                if isinstance(sub_param.default, Depends):
                    sub_dep_func = sub_param.default.dependency
                    print(f"    └─ {sub_param_name}: {sub_dep_func.__name__}()")

# Usage:
debug_dependencies(read_users)
# Output:
# Function: read_users
#   db: get_db()
```

______________________________________________________________________

## 🎓 **Key Takeaways**

1. **FastAPI uses Python's `inspect` module** to analyze function signatures and find dependencies
1. **Dependencies are resolved recursively** - sub-dependencies are resolved first
1. **Generator dependencies** (like `get_db`) are handled specially with proper cleanup
1. **Dependency caching** prevents expensive operations from running multiple times per request
1. **The `finally` block** in `get_db()` ensures database sessions are always cleaned up
1. **Type hints are crucial** for both IDE support and runtime validation
1. **One database session per request** is the recommended pattern for transaction management

Understanding FastAPI's dependency injection system helps you write more maintainable, testable, and efficient APIs. The automatic resolution, caching, and cleanup make it a powerful tool for building robust applications!
