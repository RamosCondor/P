 #Se deben calcular:
 #Promedio de temperatura por ciudad.
 #Dia mas caluroso y mas frio por ciudad.
 #Temperatura maxima y minima registrada en la semana.
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
ciudades = ["Quito", "Guayaquil", "Cuenca"]
temperaturas = [
    [15, 28, 12],  # Lunes
    [17, 30, 14],  # Martes
    [16, 29, 13],  # Miercoles
    [18, 31, 15],  # Jueves
    [19, 32, 16],  # Viernes
    [20, 33, 17],  # Sabado
    [21, 34, 18]   # Domingo
]

promedio = [0] * len(ciudades)
tempMaxima = float('-inf')
tempMinima = float('inf')

for filas in range(len(temperaturas)):
    for col in range(len(ciudades)):
        promedio[col] += temperaturas[filas][col]

print("Los promedios de las ciudades son:")
for i in range(len(ciudades)):
    print(f"El promedio de la ciudad de {ciudades[i]} es {promedio[i] / len(dias):.2f}")

print("-" * 40)

for ciudad in range(len(ciudades)):
    auxtmpmaxima = temperaturas[0][ciudad]
    auxtmpminima = temperaturas[0][ciudad]
    diaMasCaluroso = dias[0]
    diaMasFrio = dias[0]

    for dia in range(len(dias)):
        if temperaturas[dia][ciudad] > auxtmpmaxima:
            auxtmpmaxima = temperaturas[dia][ciudad]
            diaMasCaluroso = dias[dia]
        if temperaturas[dia][ciudad] < auxtmpminima:
            auxtmpminima = temperaturas[dia][ciudad]
            diaMasFrio = dias[dia]

    print(f"El dia más caluroso de la ciudad de {ciudades[ciudad]} es {diaMasCaluroso} con {auxtmpmaxima}°C")
    print(f"El dia más frío de la ciudad de {ciudades[ciudad]} es {diaMasFrio} con {auxtmpminima}°C")

print("-" * 40)

for fila in temperaturas:
    for temp in fila:
        if temp > tempMaxima:
            tempMaxima = temp
        if temp < tempMinima:
            tempMinima = temp

print(f" Temperatura maxima registrada es {tempMaxima}°C")
print(f" Temperatura minima registrada es {tempMinima}°C")
