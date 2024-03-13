import random

def adivinar_numero():
    numero_adivinar = random.randint(1,10)

    

    intento = input("Intenta adivinar el número secreto del 1 al 10 -> ")

    if  type(intento) == int:
        if intento == numero_adivinar:
            print("Lograste adivinar el Número! Felicidades\n")
        else:
            print(f"No has logrado adivinar :(, el número era {numero_adivinar}\n")

    else:
        print("Recuerda que debes ingresar un número!")
