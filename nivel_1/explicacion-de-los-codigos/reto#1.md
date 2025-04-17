
---

## 1. Detector de Palíndromos

```python
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
    # Cómo funciona: El método `.lower()` se aplica a la cadena `texto`. Esto crea una nueva cadena donde todas las letras originales se han convertido a minúsculas. Por ejemplo, "Radar" se convierte en "radar".
    # Lógica: Para que la comparación sea independiente de si las letras son mayúsculas o minúsculas, es necesario uniformizar el caso de la cadena.

    # 2. Eliminar los espacios en blanco de la cadena.
    texto = "".join(texto.split())
    # Cómo funciona: El método `.split()` sin argumentos divide la cadena `texto` en una lista de subcadenas, utilizando los espacios en blanco como delimitadores. Luego, `"".join(...)` une todos los elementos de esta lista en una nueva cadena sin ningún carácter entre ellos, eliminando así los espacios. Por ejemplo, "La ruta natural" se convierte en ["La", "ruta", "natural"] y luego en "Larutanatural".
    # Lógica: Los espacios en blanco no deben considerarse al determinar si una frase es un palíndromo.

    # 3. Invertir la cadena.
    texto_invertido = texto[::-1]
    # Cómo funciona: El slicing con `[::-1]` crea una copia invertida de la cadena `texto`. Esto es una forma concisa y eficiente de invertir una secuencia en Python. Por ejemplo, "radar" se convierte en "radar".
    # Lógica: Para verificar si es un palíndromo, necesitamos comparar la cadena original con su forma invertida.

    # 4. Comparar la cadena original (sin espacios y en minúsculas) con su versión invertida.
    if texto == texto_invertido:
        return True
    else:
        return False
    # Cómo funciona: Se utiliza una estructura condicional `if-else` para comparar la cadena procesada (`texto`) con su versión invertida (`texto_invertido`). Si son idénticas, la función devuelve `True`; de lo contrario, devuelve `False`.
    # Lógica: Un palíndromo es una cadena que se lee igual hacia adelante y hacia atrás.

# Pedir al usuario que ingrese una cadena de texto.
entrada_usuario = input("Ingresa una cadena de texto: ")
# Cómo funciona: La función `input()` muestra un mensaje al usuario en la consola y espera a que el usuario ingrese algún texto seguido de la tecla Enter. El texto ingresado se almacena en la variable `entrada_usuario` como una cadena.

# Llamar a la función para verificar si es un palíndromo.
if es_palindromo(entrada_usuario):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
# Cómo funciona: Se llama a la función `es_palindromo()` con la cadena ingresada por el usuario. El valor booleano devuelto por la función se utiliza en una estructura `if-else` para imprimir el mensaje correspondiente.

# Lógica general:
# El programa toma una entrada del usuario, la procesa para eliminar diferencias de caso y espacios, la invierte y luego compara la cadena original procesada con su versión invertida para determinar si es un palíndromo.