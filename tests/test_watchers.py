import pytest
from app.domain.errors import TicketNotFoundError

def test_watchers_without_technician(ticket_service, requester_user):
    ticket = ticket_service.create_ticket(title="Fallo de Software", requester_id=requester_user.id)
    watchers = ticket_service.watchers(ticket.id)
    assert len(watchers) == 1
    assert watchers[0].id == requester_user.id

def test_watchers_with_technician(ticket_service, requester_user, tech_user):
    ticket = ticket_service.create_ticket(title="Fallo de Software", requester_id=requester_user.id)
    ticket_service.assign(ticket.id, tech_user.id)
    watchers = ticket_service.watchers(ticket.id)
    assert len(watchers) == 2
    assert watchers[0].id == requester_user.id
    assert watchers[1].id == tech_user.id

def test_watchers_deduplication_when_same_user(ticket_service, tech_user):
    # Caso en que el técnico es también el solicitante
    ticket = ticket_service.create_ticket(title="Auto-reporte", requester_id=tech_user.id)
    ticket_service.assign(ticket.id, tech_user.id)
    watchers = ticket_service.watchers(ticket.id)
    assert len(watchers) == 1

def test_watchers_nonexistent_ticket_raises_exception(ticket_service):
    with pytest.raises(TicketNotFoundError):
        ticket_service.watchers(99999)