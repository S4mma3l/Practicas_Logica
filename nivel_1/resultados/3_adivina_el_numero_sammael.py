# Solución al Ejercicio 3: Adivina el Número
import random

def adivina_el_numero():
    """
    Juego para que el usuario adivine un número aleatorio entre 1 y 100.
    """
    # 1. Generar un número aleatorio entre 1 y 100.
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    # 2. Bucle while que continúa hasta que el usuario adivina el número.
    while not adivinado:
        try:
            # 3. Pedir al usuario que ingrese su intento.
            intento = int(input("Intenta adivinar el número: "))
            intentos += 1

            # 4. Comparar el intento del usuario con el número secreto y dar pistas.
            if intento < numero_secreto:
                print("Demasiado bajo.")
            elif intento > numero_secreto:
                print("Demasiado alto.")
            else:
                # 5. Si el intento es correcto, marcar como adivinado y mostrar un mensaje.
                adivinado = True
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Llamar a la función del juego.
adivina_el_numero()

# Lógica:
# La lógica principal es un bucle `while` que se ejecuta hasta que la condición `adivinado`
# se vuelve True. En cada iteración, se pide al usuario un intento y se compara con el
# número secreto. Se proporcionan pistas para guiar al usuario. Cuando el intento es correcto,
# se cambia el valor de `adivinado` a True, lo que termina el bucle. Se utiliza `random.randint`
# para generar el número aleatorio. También se incluye manejo de errores para asegurar que
# el usuario ingrese un número entero.