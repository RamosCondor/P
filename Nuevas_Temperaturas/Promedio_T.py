 #Se deben calcular:
 #Promedio de temperatura por ciudad.
 #Día más caluroso y más frío por ciudad.
 #Temperatura máxima y mínima registrada en la semana.
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
ciudades = ["Quito", "Guayaquil", "Cuenca"]
temperaturas = [
    [15, 28, 12],  # Lunes
    [17, 30, 14],  # Martes
    [16, 29, 13],  # Miércoles
    [18, 31, 15],  # Jueves
    [19, 32, 16],  # Viernes
    [20, 33, 17],  # Sábado
    [21, 34, 18]   # Domingo
]

# Inicialización de promedios
promedio = [0] * len(ciudades)
tempMaxima = float('-inf')
tempMinima = float('inf')

# Cálculo de promedios
for filas in range(len(temperaturas)):
    for col in range(len(ciudades)):
        promedio[col] += temperaturas[filas][col]

# Impresión de promedios
print("Los promedios de las ciudades son:")
for i in range(len(ciudades)):
    print(f"El promedio de la ciudad de {ciudades[i]} es {promedio[i] / len(dias):.2f}")

print("-" * 40)

# Determinar días más calurosos y fríos por ciudad
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

    print(f"El día más caluroso de la ciudad de {ciudades[ciudad]} es {diaMasCaluroso} con {auxtmpmaxima}°C")
    print(f"El día más frío de la ciudad de {ciudades[ciudad]} es {diaMasFrio} con {auxtmpminima}°C")

print("-" * 40)

# Determinar la temperatura máxima y mínima en general
for fila in temperaturas:
    for temp in fila:
        if temp > tempMaxima:
            tempMaxima = temp
        if temp < tempMinima:
            tempMinima = temp

print(f"La temperatura máxima registrada es {tempMaxima}°C")
print(f"La temperatura mínima registrada es {tempMinima}°C")