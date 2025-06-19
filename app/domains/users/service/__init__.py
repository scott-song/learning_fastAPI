from typing import List, Optional

from sqlalchemy.orm import Session

from .crud import user_crud
from .schemas import User, UserCreate, UserUpdate


class UserService:
    """User business logic and service layer"""

    def __init__(self):
        self.crud = user_crud

    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        """Get user by ID with business logic validation"""
        user = self.crud.get(db, id=user_id)
        if not user:
            return None
        return User.from_orm(user)

    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        user = self.crud.get_by_email(db, email=email)
        if not user:
            return None
        return User.from_orm(user)

    def create_user(self, db: Session, user_data: UserCreate) -> User:
        """Create a new user with business validation"""
        # Check if user already exists
        existing_user = self.crud.get_by_email(db, email=user_data.email)
        if existing_user:
            raise ValueError("User with this email already exists")

        # Create user
        user = self.crud.create(db, obj_in=user_data)
        return User.from_orm(user)

    def update_user(
        self, db: Session, user_id: int, user_data: UserUpdate
    ) -> Optional[User]:
        """Update user with business logic"""
        user = self.crud.get(db, id=user_id)
        if not user:
            return None

        updated_user = self.crud.update(db, db_obj=user, obj_in=user_data)
        return User.from_orm(updated_user)

    def delete_user(self, db: Session, user_id: int) -> bool:
        """Delete user with business logic"""
        user = self.crud.get(db, id=user_id)
        if not user:
            return False

        self.crud.remove(db, id=user_id)
        return True

    def get_users(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[User]:
        """Get list of users"""
        users = self.crud.get_multi(db, skip=skip, limit=limit)
        return [User.from_orm(user) for user in users]

    def authenticate_user(
        self, db: Session, email: str, password: str
    ) -> Optional[User]:
        """Authenticate user"""
        user = self.crud.authenticate(db, email=email, password=password)
        if not user:
            return None
        return User.from_orm(user)


# Create service instance
user_service = UserService()
