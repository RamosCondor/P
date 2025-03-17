temperaturas = [
    [  # Ambato 1
        [31, 32, 31, 29, 30, 33, 34],  # Semana 1
        [28, 31, 32, 30, 28, 28, 30],  # Semana 2
        [31, 33, 31, 32, 31, 30, 29],  # Semana 3
        [29, 30, 31, 32, 33, 34, 30]   # Semana 4
    ],
    [  # Quito 2
        [25, 26, 27, 28, 29, 27, 26],  
        [24, 25, 26, 27, 29, 29, 30],  
        [27, 29, 29, 30, 31, 32, 31],  
        [26, 27, 28, 29, 30, 32, 33]   
    ],
    [  # Riobamba 3
        [18, 20, 19, 21, 22, 23, 21],  
        [19, 20, 21, 22, 23, 24, 25],  
        [20, 20, 20, 20, 20, 20, 20],  
        [20, 21, 22, 23, 24, 25, 26]   
    ]
]

ciudades = ["Ambato 1", "Quito 2", "Riobamba 3"]

for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas por {ciudad}:")
    for semana in range(4): 
        suma_temperaturas = 0
        for dia in range(7): 
            suma_temperaturas += temperaturas[i][semana][dia]
        promedio = suma_temperaturas / 7
        print(f"  Semana {semana + 1}: {promedio:.2f} grados")
    print("")  