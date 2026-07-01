from app.status import DEFAULT_TICKET_STATUS, TICKET_STATUS_VALUES, TicketStatus


def test_ticket_status_contract() -> None:
    assert list(TICKET_STATUS_VALUES) == ["open", "in_progress", "resolved"]
    assert TicketStatus.OPEN.value == DEFAULT_TICKET_STATUS
    assert {s.value for s in TicketStatus} == set(TICKET_STATUS_VALUES)
