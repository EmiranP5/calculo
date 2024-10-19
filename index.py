import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Función de la calculadora de integrales definida
def calcular_integral():
    try:
        # Obtener los valores ingresados
        funcion_str = funcion_entry.get()
        limite_inferior = float(limite_inferior_entry.get())
        limite_superior = float(limite_superior_entry.get())
        
        # Definir la variable simbólica y la función
        x = sp.symbols('x')
        funcion = sp.sympify(funcion_str)
        
        # Calcular la integral definida
        integral_definida = sp.integrate(funcion, (x, limite_inferior, limite_superior))
        
        # Mostrar el resultado en la interfaz
        resultado_label.config(text=f"Resultado: {integral_definida}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Opción 1: Mostrar la ventana de la calculadora de integrales
def opcion_1():
    ventana_integral = tk.Toplevel()
    ventana_integral.title("Calculadora de Integrales Definidas")

    # Etiquetas y campos de entrada
    tk.Label(ventana_integral, text="Función (en términos de x):").grid(row=0, column=0, padx=10, pady=10)
    global funcion_entry
    funcion_entry = tk.Entry(ventana_integral)
    funcion_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(ventana_integral, text="Límite Inferior:").grid(row=1, column=0, padx=10, pady=10)
    global limite_inferior_entry
    limite_inferior_entry = tk.Entry(ventana_integral)
    limite_inferior_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(ventana_integral, text="Límite Superior:").grid(row=2, column=0, padx=10, pady=10)
    global limite_superior_entry
    limite_superior_entry = tk.Entry(ventana_integral)
    limite_superior_entry.grid(row=2, column=1, padx=10, pady=10)

    # Botón para calcular
    calcular_boton = tk.Button(ventana_integral, text="Calcular Integral", command=calcular_integral)
    calcular_boton.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Etiqueta para mostrar el resultado
    global resultado_label
    resultado_label = tk.Label(ventana_integral, text="Resultado:")
    resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Opción 2 (Funcionalidad adicional)
def opcion_2():
    messagebox.showinfo("Opción 2", "Funcionalidad para Opción 2 por agregar")

# Opción 3 (Funcionalidad adicional)
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
