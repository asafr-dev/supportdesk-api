from __future__ import annotations

from enum import StrEnum

# Canonical ticket status set for the API
TICKET_STATUS_VALUES: tuple[str, ...] = ("open", "in_progress", "resolved")
DEFAULT_TICKET_STATUS: str = "open"


class TicketStatus(StrEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
