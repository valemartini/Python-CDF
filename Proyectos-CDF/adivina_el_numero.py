from random import randint

def juego_adivina_numero():
    vidas = 5
    numero_maquina = randint(1, 100)  
    print("¡Bienvenido al juego de adivinar el número! Tienes 5 vidas.")

    while vidas > 0:
        intento = int(input("Introduce tu número (entre 1 y 100): "))
        if intento < 1 or intento > 100:
            print("Por favor, introduce un número válido entre 1 y 100.")
            continue

        if intento == numero_maquina:
            print(f"¡Felicidades! Has adivinado el número {numero_maquina}. ¡Ganaste!")
            break
        elif intento < numero_maquina:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        vidas -= 1
        if vidas > 0:
            print(f"Tienes {vidas} vidas restantes.")
        else:
            print(f"¡Has perdido! El número era {numero_maquina}.")
            break

while True:
    juego_adivina_numero()
    pregunta = input("¿Desea volver a jugar? 1- Si 2- No ->")
    if pregunta == "2":
        print("Saliendo...")
        break
