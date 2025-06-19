from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from ..crud import user_crud
from ..schemas import User, UserCreate, UserUpdate

router = APIRouter()


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of users.

    Full URL path: /api/v1/users/

    The path is built up through multiple router inclusions:
    1. In main.py: app.include_router(api_router, prefix="/api/v1")
    2. In api_router.py: api_router.include_router(
       users_router, prefix="/users", tags=["users"])
    3. In this file: @router.get("/") defines the final path segment

    So when you make a GET request to /api/v1/users/, it gets routed here.
    The "users" part comes from the prefix defined in api_router.py when
    including this router.

    Query Parameters:
    - skip: Number of records to skip (pagination offset)
    - limit: Maximum number of records to return (pagination limit)
    """
    print("read_users")
    users = user_crud.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
):
    """Create new user"""
    user = user_crud.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = user_crud.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=User)
def read_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
):
    """Get a specific user by id"""
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    return user


@router.put("/{user_id}", response_model=User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: UserUpdate,
):
    """Update a user"""
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    user = user_crud.update(db, db_obj=user, obj_in=user_in)
    return user


@router.delete("/{user_id}")
def delete_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
):
    """Delete a user"""
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system",
        )
    user_crud.remove(db, id=user_id)
    return {"message": "User deleted successfully"}
