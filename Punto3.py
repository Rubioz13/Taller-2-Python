valores_positivos = 0
valores_negativos = 0
print("Ingresa valores enteros (ingresa 0 para terminar):")
while True:
    valor = int(input())
    if valor == 0:
        break
    elif valor > 0:
        valores_positivos += 1
    else:
        valores_negativos += 1
print("Gráfico de valores ingresados:")
print("Valores positivos: " + "*" * valores_positivos)
print("Valores negativos: " + "*" * valores_negativos)