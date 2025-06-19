# Import all the models from domains, so that Base has them before being
# imported by Alembic
from app.db.database import Base  # noqa
from app.domains.items.models import Item  # noqa

# Import all domain models
from app.domains.users.models import User  # noqa
