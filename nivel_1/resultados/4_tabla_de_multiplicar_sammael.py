# Solución al Ejercicio 4: Tabla de Multiplicar
def tabla_de_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número dado del 1 al 10.

    Args:
        numero (int): El número del cual se imprimirá la tabla de multiplicar.
    """
    print(f"Tabla de multiplicar del {numero}:")
    # 1. Utilizar un bucle for para iterar del 1 al 10 (inclusive).
    for i in range(1, 11):
        # 2. Calcular el producto del número y el iterador.
        resultado = numero * i
        # 3. Imprimir el resultado en el formato deseado.
        print(f"{numero} x {i} = {resultado}")

# Pedir al usuario que ingrese un número entero.
try:
    num_usuario = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
    tabla_de_multiplicar(num_usuario)
except ValueError:
    print("Por favor, ingresa un número entero válido.")

# Lógica:
# La lógica se basa en la iteración utilizando un bucle `for`.
# La función `range(1, 11)` genera una secuencia de números del 1 al 10.
# En cada iteración, se multiplica el número ingresado por el valor actual del iterador
# y se imprime el resultado de la multiplicación.