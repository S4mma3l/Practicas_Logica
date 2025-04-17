# Solución al Ejercicio 5: Suma de Dígitos
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
    suma = 0
    # 2. Iterar sobre cada carácter (dígito) en la cadena.
    for digito in cadena_numero:
        # 3. Convertir cada dígito de nuevo a un entero y sumarlo a la variable 'suma'.
        suma += int(digito)
    # 4. Devolver la suma total de los dígitos.
    return suma

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

# Lógica:
# La lógica implica convertir el número entero a una cadena para poder acceder a cada dígito individualmente.
# Luego, se itera sobre cada carácter de la cadena, se convierte de nuevo a un entero y se acumula en una variable `suma`.