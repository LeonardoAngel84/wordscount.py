def contar_palabras(texto):
    """
    Cuenta la cantidad de palabras en un texto y la frecuencia de cada palabra.

    Args:
        texto (str): El texto a analizar.

    Returns:
        tuple: Una tupla que contiene la cantidad de palabras y un diccionario con la frecuencia de cada palabra.
    """
    # Eliminar puntuación y convertir a minúsculas
    texto = ''.join(e for e in texto if e.isalnum() or e.isspace()).lower()
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Contar la cantidad de palabras
    cantidad_palabras = len(palabras)
    
    # Contar la frecuencia de cada palabra
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    return cantidad_palabras, frecuencia_palabras

# Ejemplo de uso
texto = "Este es un ejemplo de texto. El texto es solo un ejemplo."
cantidad_palabras, frecuencia_palabras = contar_palabras(texto)

print(f"Cantidad de palabras: {cantidad_palabras}")
print("Frecuencia de cada palabra:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")