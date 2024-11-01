import advanced_alchemy.types as alchemy_types
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import Mapped, mapped_column


class Test1(UUIDAuditBase):
    """Role."""

    __tablename__ = "test1"

    data: Mapped[dict]


class Test2(UUIDAuditBase):
    """Role."""

    __tablename__ = "test2"

    data: Mapped[dict] = mapped_column(alchemy_types.JsonB, nullable=False, default={})


class Test3(UUIDAuditBase):
    """Role."""

    __tablename__ = "test3"

    data: Mapped[dict] = mapped_column(nullable=False, default={})


class Test4(UUIDAuditBase):
    """Role."""

    __tablename__ = "test4"

    data: Mapped[dict] = mapped_column(MutableDict.as_mutable(alchemy_types.JsonB))
