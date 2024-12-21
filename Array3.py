import numpy as np

def calcular_promedio(matriz):
    """
    Calcula el promedio de una matriz de números enteros.

    Args:
        matriz (list): Matriz de números enteros.

    Returns:
        float: Promedio de la matriz.
    """
    # Convertir la matriz a un arreglo de NumPy
    arreglo = np.array(matriz)

    # Calcular el promedio
    promedio = np.mean(arreglo)

    return promedio

# Crear una matriz de ejemplo
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calcular y imprimir el promedio
promedio = calcular_promedio(matriz)
print("Promedio:", promedio)