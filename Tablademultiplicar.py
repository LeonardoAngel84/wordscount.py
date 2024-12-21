import keyboard

def tabla_de_multiplicar(numero):
    """
    Genera la tabla de multiplicar de un número específico.

    Args:
        numero (int): El número para el que se generará la tabla de multiplicar.
    """
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    """
    Pide al usuario un número y genera la tabla de multiplicar correspondiente en un loop hasta que se presione la tecla Escape.
    """
    print("Presione Escape para salir.")
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            tabla_de_multiplicar(numero)
        except ValueError:
            print("Error: Debe ingresar un número entero.")
        if keyboard.is_pressed('esc'):
            break

if __name__ == "__main__":
    main()