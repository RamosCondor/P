matriz = [
    [11, 15, 13],
    [16, 15, 11],
    [17, 15, 19]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:  
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

print("Matriz: ")
for fila in matriz:
    print(fila)
fila_a_ordenar = int(input("Ingrese el numero de la fila que quiere ordenar 0-2: "))

if 0 <= fila_a_ordenar < len(matriz):
    matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Numero de fila no existe")