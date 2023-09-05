print("Ingresa la fila actual del caballo (1-8): ")
fila_caballo = int(input())

print("Ingresa la columna actual del caballo (1-8): ")
columna_caballo = int(input())

if fila_caballo < 1 or fila_caballo > 8 or columna_caballo < 1 or columna_caballo > 8:
    print("Posicion fuera de rango, recuerda que debe estar entre la posicion 1 y 8.")
else:
    movimientos_filas = [2, 2, -2, -2, 1, 1, -1, -1]
    movimientos_columnas = [1, -1, 1, -1, 2, -2, 2, -2]

    print("Posibles movimientos del caballo desde (", fila_caballo, ", ", columna_caballo, "):")

    for i in range(8):
        nueva_fila = fila_caballo + movimientos_filas[i]
        nueva_columna = columna_caballo + movimientos_columnas[i]

        if 1 <= nueva_fila <= 8 and 1 <= nueva_columna <= 8:
            print("(", nueva_fila, ", ", nueva_columna, ")")