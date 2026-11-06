from flask import Blueprint
from typing import Any

from app.modules.health.schemas import LiveResponse

bp = Blueprint("health", __name__, url_prefix="/health")

@bp.get("/live")
def live() -> dict[str, Any]:
    return LiveResponse().model_dump()