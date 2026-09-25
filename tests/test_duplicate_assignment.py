import pytest
from app.domain.errors import DuplicateAssignmentError
from app.services.notifications import WebhookNotifier

def test_duplicate_assignment_raises_error_without_side_effects(ticket_service, tech_user):
    ticket = ticket_service.create_ticket(title="Mantenimiento", requester_id=1)
    ticket_service.assign(ticket.id, tech_user.id)

    with pytest.raises(DuplicateAssignmentError):
        ticket_service.assign(ticket.id, tech_user.id)

def test_webhook_notifier_polymorphism(ticket_service_factory, tech_user):
    notifier = WebhookNotifier()
    service = ticket_service_factory(notifier=notifier)
    ticket = service.create_ticket(title="Fallo de Red", requester_id=1)

    service.assign(ticket.id, tech_user.id)

    assert len(notifier.sent_payloads) == 1
    assert notifier.sent_payloads[0]["event_type"] == "ticket_assigned"
    assert notifier.sent_payloads[0]["payload"]["ticket_id"] == ticket.id