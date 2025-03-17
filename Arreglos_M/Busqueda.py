matriz = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  
        for j in range(len(matriz[i])): 
            if matriz[i][j] == valor:
                return i+1, j+1   

valor_buscado = int(input("Ingrese el numero a buscar: "))

posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f"El numero {valor_buscado} se encuentra en la posicion {posicion} (fila, columna).")
else:
    print(f"El numero {valor_buscado} no se encontra.")