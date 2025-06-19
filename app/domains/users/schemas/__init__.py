from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    """Base user schema with shared properties"""

    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    """Schema for creating a new user"""

    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    """Schema for updating a user"""

    password: Optional[str] = None


class UserInDBBase(UserBase):
    """Base schema for user data in database"""

    id: Optional[int] = None

    class Config:
        from_attributes = True  # Pydantic v2 syntax


# Additional properties to return via API
class User(UserInDBBase):
    """Schema for user data returned by API"""

    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    """Schema for user data stored in database"""

    hashed_password: str
