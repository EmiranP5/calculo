import tkinter as tk
from tkinter import messagebox
import definidas  # Importamos el archivo definidas.py

# Opción 1: Llamar a la calculadora de integrales
def opcion_1():
    definidas.crear_ventana_integrales()

# Opción 2: Otra funcionalidad (puedes agregar más funcionalidad aquí)
def opcion_2():
    messagebox.showinfo("Opción 2", "Funcionalidad para Opción 2 por agregar")

# Opción 3: Otra funcionalidad (puedes agregar más funcionalidad aquí)
def opcion_3():
    messagebox.showinfo("Opción 3", "Funcionalidad para Opción 3 por agregar")

# Crear la ventana principal
def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Menú con Botones")
    
    # Crear los botones
    boton_1 = tk.Button(ventana, text="Opción 1 - Calculadora de Integrales", command=opcion_1)
    boton_1.pack(pady=10)

    boton_2 = tk.Button(ventana, text="Opción 2", command=opcion_2)
    boton_2.pack(pady=10)

    boton_3 = tk.Button(ventana, text="Opción 3", command=opcion_3)
    boton_3.pack(pady=10)

    # Ejecutar la ventana principal
    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()
