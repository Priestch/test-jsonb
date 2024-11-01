from __future__ import annotations

from advanced_alchemy.repository import SQLAlchemyAsyncRepository, SQLAlchemyAsyncSlugRepository

from app.db.models import Role, User, UserOauthAccount, UserRole
from app.db.models.test import Test1, Test2, Test3, Test4


class UserRepository(SQLAlchemyAsyncRepository[User]):
    """User SQLAlchemy Repository."""

    model_type = User


class UserOauthAccountRepository(SQLAlchemyAsyncRepository[UserOauthAccount]):
    """User SQLAlchemy Repository."""

    model_type = UserOauthAccount


class RoleRepository(SQLAlchemyAsyncSlugRepository[Role]):
    """User SQLAlchemy Repository."""

    model_type = Role


class UserRoleRepository(SQLAlchemyAsyncRepository[UserRole]):
    """User Role SQLAlchemy Repository."""

    model_type = UserRole


class T1(SQLAlchemyAsyncRepository[Test1]):
    """User SQLAlchemy Repository."""

    model_type = Test1


class T2(SQLAlchemyAsyncRepository[Test2]):
    """User SQLAlchemy Repository."""

    model_type = Test2


class T3(SQLAlchemyAsyncRepository[Test3]):
    """User SQLAlchemy Repository."""

    model_type = Test3


class T4(SQLAlchemyAsyncRepository[Test4]):
    """User SQLAlchemy Repository."""

    model_type = Test4
