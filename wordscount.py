import re

def contar_palabras(texto):
    
    palabras = texto.split()
    return len(palabras)

# Ejemplo de uso:
texto = "Hola mundo, esto es un ejemplo de texto."
print(contar_palabras(texto)) 