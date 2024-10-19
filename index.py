import tkinter as tk
from tkinter import messagebox

def opcion_1():
    messagebox.showinfo("Opción 1", "Has seleccionado la Opción 1")

def opcion_2():
    messagebox.showinfo("Opción 2", "Has seleccionado la Opción 2")

def opcion_3():
    messagebox.showinfo("Opción 3", "Has seleccionado la Opción 3")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Menú con Botones")
    
    # Crear los botones
    boton_1 = tk.Button(ventana, text="Opción 1", command=opcion_1)
    boton_1.pack(pady=10)

    boton_2 = tk.Button(ventana, text="Opción 2", command=opcion_2)
    boton_2.pack(pady=10)

    boton_3 = tk.Button(ventana, text="Opción 3", command=opcion_3)
    boton_3.pack(pady=10)

    # Ejecutar la ventana
    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()
