from sqlalchemy import select, func
from app.repositories.orm_models import TicketORM

class SqlAlchemyTicketRepository:
    def __init__(self, session_factory):
        self._session_factory = session_factory

    def count_by_status(self) -> dict[str, int]:
        """Retorna un diccionario con la cuenta de tickets por estado."""
        stmt = (
            select(TicketORM.status, func.count(TicketORM.id))
            .group_by(TicketORM.status)
        )
        with self._session_factory() as session:
            results = session.execute(stmt).all()
            return {status: count for status, count in results}