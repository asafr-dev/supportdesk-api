from __future__ import annotations

import datetime
import time

from sqlalchemy import insert
from sqlalchemy.orm import Session

from .models import Ticket
from .status import TicketStatus


def seed_if_empty(db: Session) -> None:
    """Seed realistic demo data if the tickets table is empty.

    This is intentionally lightweight (no users/roles in this service) but creates enough
    records to make the list/filter endpoints feel real during review.
    """

    exists = db.query(Ticket).limit(1).first()
    if exists:
        return

    templates: list[tuple[str, str]] = [
        ("Cannot reset password", "Reset link shows expired immediately on first click."),
        ("Billing page 500 error", "Visiting /billing intermittently returns 500 in production."),
        ("Feature request: export tickets", "Would love CSV export from the ticket dashboard."),
        ("Login redirect loop", "After login I get redirected back to /login repeatedly."),
        ("Emails not delivered", "Password reset emails sometimes never arrive."),
        ("Slow search results", "Searching tickets is noticeably slow with larger data sets."),
        ("Mobile layout issue", "Ticket table overflows on small screens."),
        ("Webhook retries", "Need retry handling for failed webhook deliveries."),
        ("Timezone mismatch", "Timestamps appear in a different timezone than expected."),
        ("CSV export encoding", "CSV export should default to UTF-8 and handle commas safely."),
        ("Pagination edge case", "Ticket list shows duplicates when paginating quickly."),
        ("Rate limit consideration", "API should return 429 when exceeding rate limits."),
        ("Notification preferences", "Users want per-ticket notification preferences."),
        ("Bulk status update", "Allow selecting multiple tickets and updating status."),
        ("Performance profiling", "Add basic instrumentation for slow queries."),
    ]

    statuses = (
        [TicketStatus.OPEN.value] * 6
        + [TicketStatus.IN_PROGRESS.value] * 5
        + [TicketStatus.RESOLVED.value] * 4
    )

    stmt = insert(Ticket)

    for (title, description), status in zip(templates, statuses, strict=True):
        ts = datetime.datetime.now(datetime.UTC)
        db.execute(
            stmt.values(
                title=title,
                description=description,
                status=status,
                created_at=ts,
                updated_at=ts,
            )
        )
        db.flush()
        time.sleep(0.1)

    db.commit()
