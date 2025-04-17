# Solución al Ejercicio 2: Calculadora Simple
def calculadora():
    """
    Función que realiza operaciones aritméticas básicas según la entrada del usuario.
    """
    try:
        # 1. Pedir al usuario que ingrese dos números.
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        # 2. Pedir al usuario que ingrese la operación a realizar.
        operacion = input("Ingresa la operación (+, -, *, /): ")

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
        else:
            # 5. Informar al usuario si la operación ingresada no es válida.
            print("Operación no válida.")

    except ValueError:
        print("Error: Por favor, ingresa números válidos.")

# Llamar a la función calculadora.
calculadora()

# Lógica:
# La lógica se basa en la toma de decisiones utilizando condicionales (`if`, `elif`, `else`).
# Primero, se obtienen los números y la operación del usuario.
# Luego, se evalúa la operación ingresada y se realiza el cálculo correspondiente.
# Es importante incluir una verificación para la división por cero para evitar errores.
# Se utiliza un bloque `try-except` para manejar posibles errores si el usuario ingresa
# algo que no se puede convertir a un número (ValueError).