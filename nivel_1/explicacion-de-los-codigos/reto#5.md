def suma_de_digitos(numero):
    """
    Calcula la suma de los dígitos de un número entero positivo.

    Args:
        numero (int): El número entero positivo.

    Returns:
        int: La suma de los dígitos del número.
    """
    # 1. Convertir el número a una cadena para poder iterar sobre sus dígitos.
    cadena_numero = str(numero)
    # Cómo funciona: La función `str()` convierte el número entero `numero` en una cadena de texto. Por ejemplo, si `numero` es 123, `cadena_numero` se convierte en "123".
    # Lógica: Para acceder a cada dígito individualmente, es más fácil trabajar con el número como una secuencia de caracteres.

    suma = 0
    # Cómo funciona: Se inicializa una variable `suma` en 0. Esta variable se utilizará para acumular la suma de los dígitos.
    # Lógica: Necesitamos un acumulador para ir sumando los valores de los dígitos.

    # 2. Iterar sobre cada carácter (dígito) en la cadena.
    for digito in cadena_numero:
        # Cómo funciona: El bucle `for` itera sobre cada carácter de la cadena `cadena_numero`. En cada iteración, la variable `digito` toma el valor del carácter actual. Por ejemplo, en la primera iteración, `digito` será '1', luego '2', y finalmente '3' para el número 123.
        # Lógica: Necesitamos procesar cada dígito del número.

        # 3. Convertir cada dígito de nuevo a un entero y sumarlo a la variable 'suma'.
        suma += int(digito)
        # Cómo funciona: La función `int()` convierte el carácter `digito` (que es una cadena) a un entero. Luego, el operador `+=` suma este entero al valor actual de la variable `suma`.
        # Lógica: Para realizar la suma, los dígitos (que inicialmente son caracteres en la cadena) deben convertirse a su representación numérica.

    # 4. Devolver la suma total de los dígitos.
    return suma
    # Cómo funciona: Después de que el bucle ha terminado de iterar sobre todos los dígitos, la función devuelve el valor final de la variable `suma`.
    # Lógica: El resultado de la función es la suma de todos los dígitos del número original.

# Pedir al usuario que ingrese un número entero positivo.
try:
    num_usuario = int(input("Ingresa un número entero positivo: "))
    if num_usuario < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        resultado_suma = suma_de_digitos(num_usuario)
        print(f"La suma de los dígitos de {num_usuario} es: {resultado_suma}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
    # Cómo funciona: Similar a otros ejemplos, este bloque `try-except` maneja la posible excepción si el usuario ingresa una entrada no válida. También se incluye una verificación para asegurar que el número sea positivo, según lo solicitado en el problema.
    # Lógica: Se valida la entrada del usuario y se manejan posibles errores.

# Lógica general:
# El programa toma un número entero positivo del usuario, lo convierte a una cadena para iterar sobre sus dígitos, convierte cada dígito de nuevo a un entero y los suma. Finalmente, muestra la suma resultante.