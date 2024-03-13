import random

def memoria():

    secuencia = []

    for i in range(5):
        secuencia.append(str(random.randint(1,20)))

    secuencia_str = ",".join(secuencia)

    print(f"Hola! Recuerda memorizar la siguiente secuencia de números: {secuencia_str}")


    adivina = input("\nIngresa nuevamente la secuencia que te dijo la computadora, separada por comas -> ")

    if adivina.split(',') == secuencia:
        print(f"\nHas adivinado! la secuencia es {secuencia_str} ")

    else:
        print(f"\nHas fallado, la secuencia es {secuencia_str} y tu has dicho {adivina}")

    pass