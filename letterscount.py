def contar_letras(oracion):
    """
    Cuenta la cantidad de letras en una oración.

    Args:
        oracion (str): La oración a contar.

    Returns:
        int: La cantidad de letras en la oración.
    """
    # Eliminar espacios en blanco y convertir a minúsculas
    oracion = oracion.replace(" ", "").lower()
    
    # Contar la cantidad de letras
    cantidad_letras = len(oracion)
    
    return cantidad_letras

# Ejemplo de uso
oracion = "Hola, mundo!"
print(contar_letras(oracion))