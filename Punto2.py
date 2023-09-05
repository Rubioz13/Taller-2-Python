tiempo_total_minutos = 0
while True:
    tiempo_tramo = int(input("Ingresa el tiempo de viaje del tramo (en minutos), o 0 para terminar: "))
    if tiempo_tramo == 0:
        break
    tiempo_total_minutos += tiempo_tramo
horas = tiempo_total_minutos // 60
minutos = tiempo_total_minutos % 60
print("El tiempo total de viaje es: " + str(horas) + " horas " + str(minutos) + " minutos")