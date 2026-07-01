from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from .status import TICKET_STATUS_VALUES, TicketStatus


class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class StatusPatch(BaseModel):
    status: TicketStatus = Field(
        ...,
        description=f"Ticket status: {' | '.join(TICKET_STATUS_VALUES)}",
    )
