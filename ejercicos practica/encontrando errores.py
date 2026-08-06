def crear_lista_registros_mutables():
    """
    Funcion intencional: Crear una lista de registros de usuario
    identicos (3 copias). Pero que se podrian modificar cada una de
    forma independiente.
    """

    # 1. Creamos el objeto mutable base UNA SOLA VEZ
    registro_base = {
        "id": 0,
        "nombre": "N/A",
        "rol": "invitado"
    }

    # Lista que almacenara las referencias
    lista_registros = []

    # Agregamos la referencia al mismo objeto 3 veces
    print("--- 1. Agregando la MISMA referencia 3 veces (Causa del Aliasing) ---")
    for i in range(3):
        lista_registros.append(registro_base.copy())
        print(f"ID del objeto en la posicion [{i}]: {id(lista_registros[i])}")

    print("\n--- 2. Lista Inicial ---")
    for i, reg in enumerate(lista_registros):
        print(f"Registro {i}: {reg}")

    return lista_registros


# Ejecutar la funcion con el nombre actualizado
mdict = crear_lista_registros_mutables()

print("\n--- 3. Modificando SOLO el primer registro (mdict[0]) ---")

mdict[0]["nombre"] = "Juan Perez"
mdict[0]["id"] = 101

print("\n--- 4. Resultado Inesperado ---")
for i, reg in enumerate(mdict):
    print(f"Registro {i}: {reg}")



