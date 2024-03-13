import random
def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """

    eleccion_usuario = input("Ingresa tu opción dentro de piedra, papel o tijera ->")

    lista = ["piedra","papel", "tijera"]

    eleccion_computadora = random.choice(lista)
    
    if eleccion_usuario in lista:
        if eleccion_usuario == eleccion_computadora:
            print(f"Empate! Ambos han tirado {eleccion_usuario}")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or (eleccion_usuario == "papel" and eleccion_computadora == "piedra")  or (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print(f"Has ganado! La computadora lanzó {eleccion_computadora} y tú {eleccion_usuario}")
        else:
            print(f"Has perdido! La computadora lanzó {eleccion_computadora} y tú {eleccion_usuario}")
    else:
        print("Has ingresado algo inválido! ")