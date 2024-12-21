def es_anagrama(palabra1, palabra2):
    # Eliminamos espacios y convertimos a minúsculas
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Verificamos si tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False
    
    # Creamos diccionarios para contar la frecuencia de cada letra
    freq1 = {}
    freq2 = {}
    
    # Llenamos el diccionario de frecuencias para la palabra 1
    for letra in palabra1:
        if letra in freq1:
            freq1[letra] += 1
        else:
            freq1[letra] = 1
    
    # Llenamos el diccionario de frecuencias para la palabra 2
    for letra in palabra2:
        if letra in freq2:
            freq2[letra] += 1
        else:
            freq2[letra] = 1
    
    # Comparamos los diccionarios de frecuencias
    if freq1 == freq2:
        return True
    else:
        return False

# Ejemplos de uso:
print(es_anagrama("roma", "amor"))  # True
print(es_anagrama("hello", "world"))  # False
print(es_anagrama("listen", "silent"))  # True
print(es_anagrama("triangle", "integral"))  # False