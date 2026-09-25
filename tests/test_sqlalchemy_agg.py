import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.repositories.sqlalchemy import SqlAlchemyTicketRepository
from app.repositories.orm_models import Base, TicketORM

@pytest.fixture
def sqlite_engine():
    engine = create_engine(
        "sqlite://", 
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    return engine

def test_count_by_status_persisted_in_new_session(sqlite_engine):
    SessionFactory = sessionmaker(bind=sqlite_engine)

    # 1. Sesión inicial de escritura
    with SessionFactory() as session:
        t1 = TicketORM(title="Ticket 1", requester_id=1, status="open")
        t2 = TicketORM(title="Ticket 2", requester_id=1, status="open")
        t3 = TicketORM(title="Ticket 3", requester_id=2, status="closed")
        session.add_all([t1, t2, t3])
        session.commit()

    # 2. Nueva sesión e instancia del repositorio para verificar la persistencia
    repo = SqlAlchemyTicketRepository(session_factory=SessionFactory)
    counts = repo.count_by_status()

    assert counts == {"open": 2, "closed": 1}
    assert sum(counts.values()) == 3

def test_count_by_status_empty_database(sqlite_engine):
    SessionFactory = sessionmaker(bind=sqlite_engine)
    repo = SqlAlchemyTicketRepository(session_factory=SessionFactory)
    counts = repo.count_by_status()

    assert counts == {}