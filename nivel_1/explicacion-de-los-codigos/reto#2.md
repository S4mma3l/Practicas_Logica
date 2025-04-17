
---

## 2. calculadora simple

```python

def calculadora():
    """
    Función que realiza operaciones aritméticas básicas según la entrada del usuario.
    """
    try:
        # 1. Pedir al usuario que ingrese dos números.
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        # Cómo funciona: La función `input()` pide al usuario que ingrese texto. `float()` intenta convertir ese texto a un número de punto flotante. Si la conversión falla (por ejemplo, si el usuario ingresa letras), se generará un `ValueError`.
        # Lógica: Necesitamos obtener los operandos para la operación. Usamos `float` para permitir números decimales.

        # 2. Pedir al usuario que ingrese la operación a realizar.
        operacion = input("Ingresa la operación (+, -, *, /): ")
        # Cómo funciona: Similar al paso anterior, `input()` pide al usuario que ingrese la operación deseada como una cadena.
        # Lógica: Necesitamos saber qué operación aritmética realizar.

        # 3. Utilizar condicionales para realizar la operación seleccionada.
        if operacion == '+':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif operacion == '-':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif operacion == '*':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif operacion == '/':
            # 4. Verificar si el segundo número es cero antes de realizar la división.
            if num2 == 0:
                print("Error: ¡No se puede dividir por cero!")
            else:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
            # Cómo funciona: Se utiliza una estructura `if-elif-else` para verificar qué operación ingresó el usuario. Si es '/', se realiza una verificación adicional para evitar la división por cero.
            # Lógica: Se implementan las diferentes operaciones aritméticas. Es crucial manejar el caso de la división por cero, ya que es una operación matemática indefinida y puede causar errores en el programa.

        else:
            # 5. Informar al usuario si la operación ingresada no es válida.
            print("Operación no válida.")
            # Cómo funciona: Si la `operacion` ingresada no coincide con ninguna de las operaciones válidas (+, -, *, /), se ejecuta este bloque `else`.
            # Lógica: Se proporciona retroalimentación al usuario si ingresa una operación no soportada.

    except ValueError:
        print("Error: Por favor, ingresa números válidos.")
        # Cómo funciona: El bloque `try-except` captura cualquier `ValueError` que pueda ocurrir si el usuario ingresa texto que no se puede convertir a un número en los pasos 1 o 2.
        # Lógica: Se implementa un manejo básico de errores para hacer el programa más robusto ante entradas incorrectas.

# Llamar a la función calculadora.
calculadora()
# Cómo funciona: Se ejecuta la función `calculadora()`, lo que inicia la secuencia de preguntas al usuario y la realización de la operación.

# Lógica general:
# El programa solicita dos números y una operación al usuario. Utiliza condicionales para realizar la operación seleccionada y muestra el resultado. Incluye manejo de la división por cero y de errores de entrada de números.