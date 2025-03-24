def calcular_temperatura_promedio(temperaturas):
    promedios = [sum(col) / len(col) for col in zip(*temperaturas)]
    return promedios

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
ciudades = ["Quito", "Guayaquil", "Cuenca"]

temperaturas = [
[15, 28, 12],  
[17, 30, 14],  
[16, 29, 13],  
[18, 31, 15],  
[19, 32, 16],  
[20, 33, 17],  
[21, 34, 18]   
]

temp_promedios = calcular_temperatura_promedio(temperaturas)

print("Los promedios de las ciudades son:")
for ciudad, promedio in zip(ciudades, temp_promedios):
    print(f"El promedio de la ciudad de {ciudad} es {promedio:.2f}")