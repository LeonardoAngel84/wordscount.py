import numpy as np

def calcular_promedio(matriz):
    # Convertir la matriz a un arreglo de NumPy
    arreglo = np.array(matriz)

    # Calcular el promedio
    promedio = np.mean(arreglo)
    
    suma = 0
    elementos = 0
    for fila in matriz:
        for numero in fila:
            suma += numero
            elementos += 1
    promedio = suma / elementos
    return promedio

# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
promedio = calcular_promedio(matriz)
print("El valor promedio es: ", promedio)