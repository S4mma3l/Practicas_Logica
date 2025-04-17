def tabla_de_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número dado del 1 al 10.

    Args:
        numero (int): El número del cual se imprimirá la tabla de multiplicar.
    """
    print(f"Tabla de multiplicar del {numero}:")
    # Cómo funciona: Se imprime un encabezado indicando de qué número es la tabla. La f-string permite insertar el valor de la variable `numero` directamente en la cadena.
    # Lógica: Es útil indicar al usuario para qué número se está mostrando la tabla.

    # 1. Utilizar un bucle for para iterar del 1 al 10 (inclusive).
    for i in range(1, 11):
        # Cómo funciona: `range(1, 11)` genera una secuencia de números enteros desde 1 hasta 10 (el segundo argumento no se incluye). El bucle `for` itera sobre cada número en esta secuencia, asignando el valor actual a la variable `i` en cada iteración.
        # Lógica: Necesitamos multiplicar el número dado por cada entero del 1 al 10 para obtener la tabla de multiplicar estándar.

        # 2. Calcular el producto del número y el iterador.
        resultado = numero * i
        # Cómo funciona: En cada iteración del bucle, se multiplica el `numero` pasado a la función por el valor actual de `i`. El resultado se almacena en la variable `resultado`.
        # Lógica: Esta es la operación fundamental para generar la tabla de multiplicar.

        # 3. Imprimir el resultado en el formato deseado.
        print(f"{numero} x {i} = {resultado}")
        # Cómo funciona: Se utiliza un f-string para formatear la salida de cada línea de la tabla de multiplicar, mostrando el número original, el multiplicador (`i`), el signo de multiplicación (=) y el `resultado`.
        # Lógica: Presentar la tabla de multiplicar de forma clara y legible facilita su comprensión.

# Pedir al usuario que ingrese un número entero.
try:
    num_usuario = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
    tabla_de_multiplicar(num_usuario)
except ValueError:
    print("Por favor, ingresa un número entero válido.")
    # Cómo funciona: El bloque `try-except` intenta convertir la entrada del usuario a un entero. Si falla (por ejemplo, si el usuario ingresa texto), se captura el `ValueError` y se muestra un mensaje de error.
    # Lógica: Se implementa un manejo de errores para asegurar que el programa no falle si el usuario ingresa una entrada no numérica.

# Lógica general:
# El programa pide al usuario un número entero y luego utiliza un bucle `for` para iterar del 1 al 10, calculando y mostrando el producto del número ingresado por cada valor en el rango.