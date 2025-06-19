from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base user schema with shared properties"""

    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """Schema for creating a new user"""

    email: EmailStr
    password: str


class UserUpdate(UserBase):
    """Schema for updating a user"""

    password: Optional[str] = None


class UserInDBBase(UserBase):
    """Base schema for user data in database"""

    id: Optional[int] = None

    class Config:
        from_attributes = True  # Pydantic v2 syntax


class User(UserInDBBase):
    """Schema for user data returned by API"""

    pass


class UserInDB(UserInDBBase):
    """Schema for user data stored in database"""

    hashed_password: str
