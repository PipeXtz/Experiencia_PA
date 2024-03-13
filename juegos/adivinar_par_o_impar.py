import random

def adivinar_par_o_impar():
    
    intento = input("Intenta adivinar si el número secreto es par o impar -> ")

    numero = random.randint(1,100) 

    if intento != "par" and intento != "impar":
        print("Eso no es válido, recuerda ingresar par o impar")
        return

    if numero % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    
    if intento == paridad:
        print(f"Felicitaciones! El número es {numero} y sí es {paridad}")
    else:
        print(f"Has fallado! El número es {numero} y es {paridad}")
    pass