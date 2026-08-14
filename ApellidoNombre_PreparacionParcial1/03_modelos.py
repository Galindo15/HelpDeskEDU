
class Usuario:

    def __init__(self, id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"Usuario: {self.id} | {self.nombre} | {self.email} | Rol: {self.rol}"


class Ticket:

    ESTADOS_VALIDOS = [
        "Open",
        "In Progress",
        "Resolved",
        "Closed",
        "Cancelled"
    ]

    def __init__(
        self,
        id,
        titulo,
        categoria,
        prioridad,
        solicitante,
        tecnico=None,
        status="Open"
    ):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = tecnico
        self._status = status

    def __str__(self):
        tecnico_nombre = (
            self.tecnico.nombre
            if self.tecnico
            else "Sin técnico asignado"
        )

        return (
            f"Ticket: {self.id} | "
            f"{self.titulo} | "
            f"Categoría: {self.categoria} | "
            f"Prioridad: {self.prioridad} | "
            f"Solicitante: {self.solicitante.nombre} | "
            f"Técnico: {tecnico_nombre} | "
            f"Estado: {self._status}"
        )

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            print(f"Error: '{nuevo_estado}' no es un estado válido.")
            return False

        self._status = nuevo_estado
        print(f"Estado cambiado a: {nuevo_estado}")
        return True

    def asignar_tecnico(self, tecnico):
        if tecnico.rol.lower() != "technician":
            print("Error: el usuario no tiene el rol de technician.")
            return False

        self.tecnico = tecnico
        print(f"Técnico {tecnico.nombre} asignado correctamente.")
        return True


# Crear usuarios
usuario1 = Usuario(
    1,
    "Carlos López",
    "carlos@gmail.com",
    "user"
)

usuario2 = Usuario(
    2,
    "Ana Martínez",
    "ana@gmail.com",
    "technician"
)


# Crear tres tickets
ticket1 = Ticket(
    1,
    "Computadora no enciende",
    "Hardware",
    "High",
    usuario1
)

ticket2 = Ticket(
    2,
    "Error en Windows",
    "Software",
    "Medium",
    usuario1
)

ticket3 = Ticket(
    3,
    "Problema de conexión",
    "Network",
    "Critical",
    usuario1
)


# Guardar objetos en una lista
tickets = [
    ticket1,
    ticket2,
    ticket3
]


# Mostrar usuarios
print("=== USUARIOS ===")
print(usuario1)
print(usuario2)


# Mostrar tickets
print("\n=== TICKETS ===")

for ticket in tickets:
    print(ticket)


# Asignar técnico
print("\n=== ASIGNAR TÉCNICO ===")
ticket1.asignar_tecnico(usuario2)


# Cambiar estado
print("\n=== CAMBIAR ESTADO ===")
ticket1.cambiar_estado("In Progress")


# Intentar colocar un estado no permitido
print("\n=== ESTADO NO PERMITIDO ===")
ticket1.cambiar_estado("En espera")


# Mostrar ticket actualizado
print("\n=== TICKET ACTUALIZADO ===")
print(ticket1)