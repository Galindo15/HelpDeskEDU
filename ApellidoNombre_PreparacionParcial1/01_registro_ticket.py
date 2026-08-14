
print("=== REGISTRO DE TICKET ===")

# Solicitar número de ticket
while True:
    try:
        numero = int(input("Número de ticket: "))
        break
    except ValueError:
        print("Error: el número de ticket debe ser un número entero.")
        
        # Solicitar campos obligatorios
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
    # Categoría
categorias_validas = ["General", "Hardware", "Software", "Network"]

while True:
    categoria = input("Categoría (General, Hardware, Software, Network): ").strip()

    categoria_encontrada = None

    for categoria_valida in categorias_validas:
        if categoria.lower() == categoria_valida.lower():
            categoria_encontrada = categoria_valida
            break

    if categoria_encontrada:
        categoria = categoria_encontrada
        break

    print("Error: categoría no válida.")
    # Prioridad
prioridades_validas = ["Low", "Medium", "High", "Critical"]

while True:
    prioridad = input("Prioridad (Low, Medium, High, Critical): ").strip()

    prioridad_encontrada = None

    for prioridad_valida in prioridades_validas:
        if prioridad.lower() == prioridad_valida.lower():
            prioridad_encontrada = prioridad_valida
            break

    if prioridad_encontrada:
        prioridad = prioridad_encontrada
        break

    print("Error: prioridad no válida.")
    # Crear diccionario
ticket = {
    "numero": numero,
    "solicitante": solicitante,
    "titulo": titulo,
    "descripcion": descripcion,
    "categoria": categoria,
    "prioridad": prioridad,
    "status": "Open"
}