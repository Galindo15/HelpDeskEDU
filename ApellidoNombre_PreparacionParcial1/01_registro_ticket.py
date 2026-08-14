
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