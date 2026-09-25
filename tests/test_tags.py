import pytest
from app.models.entities import Ticket
from app.domain.errors import ValidationError

def test_add_tag_normalization_and_deduplication():
    ticket = Ticket(id=1, title="Error en Red", requester_id=10)
    ticket.add_tag("  URGENTE  ")
    ticket.add_tag("urgente")
    assert ticket.tags == ("urgente",)

def test_add_tag_rejects_empty_and_whitespace():
    ticket = Ticket(id=1, title="Error en Red", requester_id=10)
    with pytest.raises(ValidationError):
        ticket.add_tag("   ")

def test_tags_instance_independence():
    t1 = Ticket(id=1, title="Ticket 1", requester_id=1)
    t2 = Ticket(id=2, title="Ticket 2", requester_id=2)
    t1.add_tag("redes")
    assert "redes" in t1.tags
    assert "redes" not in t2.tags

def test_tags_property_reassignment_fails():
    ticket = Ticket(id=1, title="Ticket 1", requester_id=1)
    with pytest.raises(AttributeError):
        ticket.tags = ("nueva_etiqueta",)