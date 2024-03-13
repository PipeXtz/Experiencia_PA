import random
def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """

    puntuacion_usuario = 0
    puntuacion_computadora = 0
    lanzamiento = 1

    while puntuacion_usuario < 30 and puntuacion_computadora < 30:
        
        lanzar_usuario = input("Apreta Enter para lanzar el dado -> ")

        if lanzar_usuario == "":
            print(f"\n---- LANZAMIENTO {lanzamiento} ----")
            tiro_usuario = random.randint(1,6)
            tiro_computadora = random.randint(1,6)

            puntuacion_computadora += tiro_computadora
            puntuacion_usuario += tiro_usuario

            print(f"\nTu dado ha sacado un {tiro_usuario}")
            print(f"La computadora ha sacado un {tiro_computadora}\n")

            print(f"Tu puntuación total es {puntuacion_usuario}")
            print(f"La puntuación total de la computadora es {puntuacion_computadora}\n")

            lanzamiento += 1
        else:
            print("Recuerda que debes apretar enter!\n")

    if puntuacion_usuario >= 30:
        print("Has ganado! :)")
    else:
        print("Ha ganado la computadora! :(")