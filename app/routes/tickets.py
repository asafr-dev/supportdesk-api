from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import Select, or_, select
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Ticket
from ..schemas import StatusPatch, TicketOut, TicketStatus

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("", response_model=list[TicketOut])
def list_tickets(
    status_: TicketStatus | None = Query(default=None, alias="status"),
    q: str | None = Query(default=None, min_length=1, max_length=200),
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
) -> list[TicketOut]:
    stmt: Select[tuple[Ticket]] = (
        select(Ticket).order_by(Ticket.updated_at.desc()).limit(limit).offset(offset)
    )

    if status_ is not None:
        stmt = stmt.where(Ticket.status == status_.value)

    if q is not None:
        pattern = f"%{q}%"
        stmt = stmt.where(or_(Ticket.title.ilike(pattern), Ticket.description.ilike(pattern)))

    tickets = list(db.execute(stmt).scalars().all())
    return [TicketOut.model_validate(t) for t in tickets]


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)) -> TicketOut:
    t = db.get(Ticket, ticket_id)
    if not t:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return TicketOut.model_validate(t)


@router.patch("/{ticket_id}/status", response_model=TicketOut)
def patch_status(
    ticket_id: int,
    body: StatusPatch,
    db: Session = Depends(get_db),
) -> TicketOut:
    t = db.get(Ticket, ticket_id)
    if not t:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    t.status = body.status.value
    db.add(t)
    db.flush()
    db.refresh(t)
    return TicketOut.model_validate(t)
