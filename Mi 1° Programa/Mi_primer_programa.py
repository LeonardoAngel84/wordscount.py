import tkinter as tk

def mostrar_mensaje():
    nombre = "LEONARDO"
    mensaje = "¡Hola Mundo!"
    texto_saludo.config(text=f"{nombre}\n{mensaje}")

def cerrar_ventana():
    ventana.destroy()

# Crear la ventana
ventana = tk.Tk()

# Configurar la ventana
ventana.title("ESTE ES hMI PRIMER PROGRAMA")
ventana.geometry("300x200")

# Crear un label para mostrar el saludo
texto_saludo = tk.Label(ventana, text="", font=("Arial Black", 20))
texto_saludo.pack(pady=50)

# Crear un botón para cerrar la ventana
boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()

# Llamar a la función para mostrar el mensaje de saludo
mostrar_mensaje()

# Iniciar el bucle de eventos
ventana.mainloop()