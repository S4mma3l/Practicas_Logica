import random

def adivina_el_numero():
    """
    Juego para que el usuario adivine un número aleatorio entre 1 y 100.
    """
    # 1. Generar un número aleatorio entre 1 y 100.
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    # Cómo funciona: `random.randint(1, 100)` genera un número entero aleatorio dentro del rango especificado (inclusive). Las variables `intentos` se inicializan en 0 para contar los intentos del usuario, y `adivinado` en `False` para controlar el bucle del juego.
    # Lógica: Necesitamos un número secreto que el usuario debe adivinar. La librería `random` es útil para generar números aleatorios.

    print("¡Bienvenido al juego Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    # 2. Bucle while que continúa hasta que el usuario adivina el número.
    while not adivinado:
        try:
            # 3. Pedir al usuario que ingrese su intento.
            intento = int(input("Intenta adivinar el número: "))
            intentos += 1
            # Cómo funciona: `input()` pide al usuario un número como texto, y `int()` intenta convertirlo a un entero. Si la conversión falla, se genera un `ValueError`. Se incrementa el contador de `intentos` en cada iteración.
            # Lógica: El juego debe continuar hasta que el usuario acierte el número secreto. Un bucle `while` es apropiado para esta situación.

            # 4. Comparar el intento del usuario con el número secreto y dar pistas.
            if intento < numero_secreto:
                print("Demasiado bajo.")
            elif intento > numero_secreto:
                print("Demasiado alto.")
            else:
                # 5. Si el intento es correcto, marcar como adivinado y mostrar un mensaje.
                adivinado = True
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            # Cómo funciona: Se utilizan estructuras `if-elif-else` para comparar el `intento` del usuario con el `numero_secreto`. Se proporcionan mensajes guía ("Demasiado bajo", "Demasiado alto"). Si el intento es correcto, se establece `adivinado` en `True`, lo que terminará el bucle.
            # Lógica: Proporcionar retroalimentación al usuario ayuda a que el juego sea jugable. Cuando el usuario adivina correctamente, el juego termina.

        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            # Cómo funciona: El bloque `try-except` maneja el caso en que el usuario ingresa algo que no se puede convertir a un entero.
            # Lógica: Se implementa un manejo de errores para asegurar que el programa no se detenga si el usuario ingresa una entrada no válida.

# Llamar a la función del juego.
adivina_el_numero()
# Cómo funciona: Se ejecuta la función `adivina_el_numero()`, lo que inicia el juego.

# Lógica general:
# El programa genera un número secreto aleatorio. Luego, entra en un bucle donde pide al usuario que adivine el número, proporciona pistas y termina cuando el usuario acierta. Se cuenta el número de intentos.