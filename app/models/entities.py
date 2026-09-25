from dataclasses import dataclass, field
from app.domain.errors import ValidationError

@dataclass
class Ticket:
    id: int
    title: str
    requester_id: int
    assignee_id: int | None = None
    status: str = "open"
    # Campo privado no expuesto en init ni repr
    _tags: list[str] = field(default_factory=list, init=False, repr=False)

    @property
    def tags(self) -> tuple[str, ...]:
        """Expone las etiquetas como una tupla inmutable de solo lectura."""
        return tuple(self._tags)

    def add_tag(self, tag: str) -> None:
        """Normaliza, valida y agrega una etiqueta evitando duplicados."""
        if not isinstance(tag, str):
            raise ValidationError("La etiqueta debe ser una cadena de texto.")
            
        normalized = tag.strip().lower()
        if not normalized:
            raise ValidationError("La etiqueta no puede estar vacía ni contener solo espacios.")
            
        if normalized not in self._tags:
            self._tags.append(normalized)