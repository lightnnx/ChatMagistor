from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.control_plane.database import get_db
from apps.control_plane.models import Node


router = APIRouter(
    prefix="/api/v1/nodes",
    tags=["Nodes"],
)


@router.get("/")
async def list_nodes(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Node).order_by(Node.created_at.desc())
    )

    nodes = result.scalars().all()

    return [
        {
            "id": str(node.id),
            "name": node.name,
            "hostname": node.hostname,
            "role": node.role.value,
            "status": node.status.value,
            "cpu_cores": node.cpu_cores,
            "ram_mb": node.ram_mb,
            "active_accounts": node.active_accounts,
            "last_heartbeat": node.last_heartbeat,
        }
        for node in nodes
    ]
