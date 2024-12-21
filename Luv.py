import time

def pregunta():
    respuesta = input("Quieres ser mi novia? (Responde 'Sí Quiero' o 'No quiero'): ")
    if respuesta.lower() == "sí quiero":
        print("Lo sabía que ibas a aceptar, ahora ya somos novios. Te amo. 😍❤️")
    else:
        print("No quiero")
        escape_texto("No quiero")

def escape_texto(texto):
    for i in range(len(texto)):
        print(texto[i], end='', flush=True)
        time.sleep(0.1)
    print()

pregunta()
