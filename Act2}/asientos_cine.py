
def crear_sala():
    filas = int(input("Ingrese el número de filas del cine: "))
    columnas = int(input("Ingrese el número de columnas (asientos por fila): "))

    sala = []
    for i in range(filas):
        fila = ["L"] * columnas
        sala.append(fila)

    return sala, filas, columnas


def mostrar_sala(sala):
    print("\nEstado actual de la sala:\n")
    for fila in sala:
        print(" ".join(fila))
    print()


def asiento_valido(fila, columna, filas, columnas):
    if 0 <= fila < filas and 0 <= columna < columnas:
        return True
    else:
        return False


def reservar_asiento(sala, filas, columnas):
    try:
        fila = int(input("Ingrese la fila del asiento: "))
        columna = int(input("Ingrese la columna del asiento: "))

        fila -= 1
        columna -= 1

        if asiento_valido(fila, columna, filas, columnas):

            if sala[fila][columna] == "L":
                sala[fila][columna] = "X"
                print("Asiento reservado correctamente.\n")
            else:
                print("El asiento ya está ocupado.\n")

        else:
            print("Ese asiento no existe.\n")

    except ValueError:
        print("Debe ingresar números válidos.\n")


def liberar_asiento(sala, filas, columnas):
    try:
        fila = int(input("Ingrese la fila del asiento: "))
        columna = int(input("Ingrese la columna del asiento: "))

        fila -= 1
        columna -= 1

        if asiento_valido(fila, columna, filas, columnas):

            if sala[fila][columna] == "X":
                sala[fila][columna] = "L"
                print("Asiento liberado correctamente.\n")
            else:
                print("El asiento ya está libre.\n")

        else:
            print("Ese asiento no existe.\n")

    except ValueError:
        print("Debe ingresar números válidos.\n")


def contar_asientos(sala):
    libres = 0
    ocupados = 0

    for fila in sala:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            elif asiento == "X":
                ocupados += 1

    print("\nEstadísticas de la sala:")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}\n")



sala, filas, columnas = crear_sala()

opcion = 0

while opcion != 5:
    print("===== MENÚ DEL CINE =====")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        print()

        if opcion == 1:
            mostrar_sala(sala)

        elif opcion == 2:
            reservar_asiento(sala, filas, columnas)

        elif opcion == 3:
            liberar_asiento(sala, filas, columnas)

        elif opcion == 4:
            contar_asientos(sala)

        elif opcion == 5:
            print("Saliendo del sistema...")

        else:
            print("Opción no válida.\n")

    except ValueError:
        print("Debe ingresar un número válido.\n")
