# Solución al Ejercicio 6: Encontrando el Mayor
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

# Pedir al usuario que ingrese tres números.
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    numero3 = float(input("Ingresa el tercer número: "))

    mayor = encontrar_el_mayor(numero1, numero2, numero3)
    print(f"El mayor de los tres números es: {mayor}")

except ValueError:
    print("Por favor, ingresa números válidos.")

# Lógica:
# La lógica se basa en una serie de comparaciones utilizando las sentencias `if`, `elif` y `else`.
# Se comparan los números entre sí para determinar cuál cumple la condición de ser mayor o igual que los otros dos.