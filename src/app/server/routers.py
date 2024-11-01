"""Application Modules."""
from __future__ import annotations

from typing import TYPE_CHECKING

from litestar import get
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.test import Test1, Test2, Test3, Test4
from app.domain.accounts.repositories import T1, T2, T3, T4

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler


@get("/")
async def index(db_session: AsyncSession) -> str:
    print("index1112")
    # t1 = T1(session=db_session)
    # t2 = T2(session=db_session)
    t3 = T3(session=db_session)
    # t4 = T4(session=db_session)
    # await t1.get_or_upsert(id="bc30c8fe-d78b-4b92-b125-7ecc7ab80fda", data={"name": "gaopeng"})
    # await t2.get_or_upsert(id="bc30c8fe-d78b-4b92-b125-7ecc7ab80fda", data={"name": "gaopeng"})
    await t3.get_or_upsert(id="bc30c8fe-d78b-4b92-b125-7ecc7ab80fda", data={"name": "gaopeng"})
    # await t4.get_or_upsert(id="bc30c8fe-d78b-4b92-b125-7ecc7ab80fda", data={"name": "gaopeng"})
    await db_session.commit()
    return "Hello, world!"


route_handlers: list[ControllerRouterHandler] = [
    # AccessController,
    # UserController,
    # TeamController,
    # UserRoleController,
    # #  TeamInvitationController,
    # TeamMemberController,
    # TagController,
    # SystemController,
    # WebController,
    index,
]
