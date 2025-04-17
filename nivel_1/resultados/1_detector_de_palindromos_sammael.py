# Solución al Ejercicio 1: Detector de Palíndromos
def es_palindromo(texto):
    """
    Función que determina si una cadena de texto es un palíndromo.

    Args:
        texto (str): La cadena de texto a verificar.

    Returns:
        bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    # 1. Convertir la cadena a minúsculas para ignorar diferencias de caso.
    texto = texto.lower()
    # 2. Eliminar los espacios en blanco de la cadena.
    texto = "".join(texto.split())
    # 3. Invertir la cadena.
    texto_invertido = texto[::-1]
    # 4. Comparar la cadena original (sin espacios y en minúsculas) con su versión invertida.
    if texto == texto_invertido:
        return True
    else:
        return False

# Pedir al usuario que ingrese una cadena de texto.
entrada_usuario = input("Ingresa una cadena de texto: ")

# Llamar a la función para verificar si es un palíndromo.
if es_palindromo(entrada_usuario):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

# Lógica:
# La lógica principal es comparar la cadena original con su versión invertida.
# Para hacer una comparación justa, primero se estandariza la cadena convirtiéndola a minúsculas
# y eliminando los espacios, ya que estos no afectan si una frase es un palíndromo.
# La inversión de la cadena se logra utilizando el slicing con un paso de -1 (`[::-1]`).
# Finalmente, se compara la cadena original con la invertida y se devuelve True o False según corresponda.
# Ejemplo de uso:
# Si el usuario ingresa "Anita lava la tina", el programa debería imprimir "Es un palíndromo".
# Si el usuario ingresa "Hola mundo", el programa debería imprimir "No es un palíndromo".