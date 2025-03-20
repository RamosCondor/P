import random

numero_aleatorio = random.randint(1, 50)
intentos = 5

for i in range(intentos):
    numero = int(input(f"Adivina el numero entre 1 y 50. Tienes {intentos - i} intentos restantes: "))

    if intentos < numero_aleatorio:
        print("Muy bajo")
    elif intentos > numero_aleatorio:
        print("Muy alto")
    else:
        print(f"Adivinaste. Es {numero_aleatorio}")
        break
else:
    print(f"Terminaste tus intentos. El numero era {numero_aleatorio}")