
---

## 6. encontrar el mayor

```python
def encontrar_el_mayor(num1, num2, num3):
    """
    Determina cuál de tres números es el mayor.

    Args:
        num1 (float): El primer número.
        num2 (float): El segundo número.
        num3 (float): El tercer número.

    Returns:
        float: El mayor de los tres números.
    """
    # 1. Utilizar condicionales para comparar los números.
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    # Cómo funciona: Se utiliza una estructura condicional `if-elif-else` para comparar los tres números.
    #   - El primer `if` verifica si `num1` es mayor o igual a `num2` Y mayor o igual a `num3`. Si ambas condiciones son verdaderas, `num1` es el mayor y se devuelve.
    #   - El `elif` se evalúa solo si la primera condición es falsa. Verifica si `num2` es mayor o igual a `num1` Y mayor o igual a `num3`. Si ambas son verdaderas, `num2` es el mayor y se devuelve.
    #   - El `else` se ejecuta si las dos condiciones anteriores son falsas. En este caso, `num3` debe ser el mayor (o igual al mayor si hay duplicados), y se devuelve.
    # Lógica: Se realizan comparaciones lógicas (`and`) y relacionales (`>=`) para determinar el número más grande entre los tres.

# Pedir al usuario que ingrese tres números.
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    numero3 = float(input("Ingresa el tercer número: "))
    # Cómo funciona: Se utiliza la función `input()` para obtener tres entradas del usuario, y `float()` intenta convertir cada entrada a un número de punto flotante.
    # Lógica: Necesitamos tres números del usuario para comparar. Usar `float` permite tanto números enteros como decimales.

    mayor = encontrar_el_mayor(numero1, numero2, numero3)
    print(f"El mayor de los tres números es: {mayor}")
    # Cómo funciona: Se llama a la función `encontrar_el_mayor()` con los tres números ingresados por el usuario. El valor devuelto (el mayor número) se almacena en la variable `mayor` y luego se imprime en la consola.
    # Lógica: El resultado de la comparación se muestra al usuario.

except ValueError:
    print("Por favor, ingresa números válidos.")
    # Cómo funciona: El bloque `try-except` captura cualquier `ValueError` que pueda ocurrir si el usuario ingresa una entrada no numérica.
    # Lógica: Se incluye manejo de errores para hacer el programa más robusto.

# Lógica general:
# El programa toma tres números como entrada del usuario y luego utiliza sentencias condicionales para compararlos e identificar el mayor de ellos. El número mayor se imprime en la consola.