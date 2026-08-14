

tickets = []

categorias_validas = ["General", "Hardware", "Software", "Network"]
prioridades_validas = ["Low", "Medium", "High", "Critical"]


def pedir_opcion():
    print("\n=== HELP DESK ===")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Resumen por prioridad")
    print("5. Salir")

    return input("Seleccione una opción: ").strip()


def registrar_ticket():
    print("\n=== REGISTRAR TICKET ===")

    while True:
        try:
            numero = int(input("Número de ticket: "))
            break
        except ValueError:
            print("Error: debe ingresar un número entero.")

    while True:
        solicitante = input("Solicitante: ").strip()

        if solicitante:
            break

        print("Error: el solicitante no puede estar vacío.")

    while True:
        titulo = input("Título: ").strip()

        if titulo:
            break

        print("Error: el título no puede estar vacío.")

    while True:
        descripcion = input("Descripción: ").strip()

        if descripcion:
            break

        print("Error: la descripción no puede estar vacía.")

    while True:
        categoria = input(
            "Categoría (General, Hardware, Software, Network): "
        ).strip()

        categoria_encontrada = None

        for categoria_valida in categorias_validas:
            if categoria.lower() == categoria_valida.lower():
                categoria_encontrada = categoria_valida
                break

        if categoria_encontrada:
            categoria = categoria_encontrada
            break

        print("Error: categoría no válida.")

    while True:
        prioridad = input(
            "Prioridad (Low, Medium, High, Critical): "
        ).strip()

        prioridad_encontrada = None

        for prioridad_valida in prioridades_validas:
            if prioridad.lower() == prioridad_valida.lower():
                prioridad_encontrada = prioridad_valida
                break

        if prioridad_encontrada:
            prioridad = prioridad_encontrada
            break

        print("Error: prioridad no válida.")

    ticket = {
        "numero": numero,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open"
    }

    tickets.append(ticket)

    print("\nTicket registrado correctamente.")


def listar_tickets():
    print("\n=== LISTA DE TICKETS ===")

    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    for ticket in tickets:
        print("-" * 40)
        print(f"Número: {ticket['numero']}")
        print(f"Solicitante: {ticket['solicitante']}")
        print(f"Título: {ticket['titulo']}")
        print(f"Categoría: {ticket['categoria']}")
        print(f"Prioridad: {ticket['prioridad']}")
        print(f"Estado: {ticket['status']}")

    print("-" * 40)
    print(f"Total de tickets: {len(tickets)}")


def buscar_por_solicitante():
    print("\n=== BUSCAR POR SOLICITANTE ===")

    nombre = input("Ingrese el nombre del solicitante: ").strip()

    encontrados = 0

    for ticket in tickets:
        if ticket["solicitante"].lower() == nombre.lower():
            print("-" * 40)
            print(f"Número: {ticket['numero']}")
            print(f"Solicitante: {ticket['solicitante']}")
            print(f"Título: {ticket['titulo']}")
            print(f"Prioridad: {ticket['prioridad']}")
            print(f"Estado: {ticket['status']}")

            encontrados += 1

    if encontrados == 0:
        print("No se encontraron tickets para ese solicitante.")
    else:
        print(f"\nTickets encontrados: {encontrados}")


def mostrar_resumen():
    print("\n=== RESUMEN POR PRIORIDAD ===")

    low = 0
    medium = 0
    high = 0
    critical = 0

    for ticket in tickets:
        if ticket["prioridad"].lower() == "low":
            low += 1
        elif ticket["prioridad"].lower() == "medium":
            medium += 1
        elif ticket["prioridad"].lower() == "high":
            high += 1
        elif ticket["prioridad"].lower() == "critical":
            critical += 1

    print(f"Low: {low}")
    print(f"Medium: {medium}")
    print(f"High: {high}")
    print(f"Critical: {critical}")
    print(f"Total: {len(tickets)}")


def ejecutar_menu():
    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_ticket()

        elif opcion == "2":
            listar_tickets()

        elif opcion == "3":
            buscar_por_solicitante()

        elif opcion == "4":
            mostrar_resumen()

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_menu()