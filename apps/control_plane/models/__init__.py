import enum
import uuid

from datetime import datetime, timezone

from sqlalchemy import (
    String,
    DateTime,
    Enum,
    Integer,
    Boolean,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from apps.control_plane.database import Base


def utc_now():
    return datetime.now(timezone.utc)


class NodeRole(str, enum.Enum):
    CONTROL = "control"
    WORKER = "worker"
    STORAGE = "storage"
    API = "api"


class NodeStatus(str, enum.Enum):
    PENDING = "pending"
    ONLINE = "online"
    OFFLINE = "offline"
    DISABLED = "disabled"


class Node(Base):
    __tablename__ = "nodes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[NodeRole] = mapped_column(
        Enum(NodeRole, name="node_role"),
        nullable=False,
    )

    status: Mapped[NodeStatus] = mapped_column(
        Enum(NodeStatus, name="node_status"),
        default=NodeStatus.PENDING,
        nullable=False,
    )

    cpu_cores: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    ram_mb: Mapped[int] = mapped_column(
        Integer,
        default=1024,
    )

    active_accounts: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    certificate_fingerprint: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True,
    )

    last_heartbeat: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )
