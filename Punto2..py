tiempo_total_minutos = 1
suma = 0
while tiempo_total_minutos != 0:
    tiempo_total_minutos = int (input("ingresa el tiempo del viaje o ingresa 0 para terminar: "))
    if tiempo_total_minutos >= 0:
        suma = suma + tiempo_total_minutos
    horas = suma // 60
    minutos = suma % 60
    print("el tiempo total del viaje es: " + str(horas) + "horas" + str(minutos) + "minutos" )