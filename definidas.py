import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Función para crear la ventana y calcular la integral definida
def crear_ventana_integrales():
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

    # Crear la ventana para la calculadora de integrales
    ventana = tk.Toplevel()
    ventana.title("Calculadora de Integrales Definidas")

    # Etiquetas y campos de entrada
    tk.Label(ventana, text="Función (en términos de x):").grid(row=0, column=0, padx=10, pady=10)
    funcion_entry = tk.Entry(ventana)
    funcion_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(ventana, text="Límite Inferior:").grid(row=1, column=0, padx=10, pady=10)
    limite_inferior_entry = tk.Entry(ventana)
    limite_inferior_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(ventana, text="Límite Superior:").grid(row=2, column=0, padx=10, pady=10)
    limite_superior_entry = tk.Entry(ventana)
    limite_superior_entry.grid(row=2, column=1, padx=10, pady=10)

    # Botón para calcular la integral
    calcular_boton = tk.Button(ventana, text="Calcular Integral", command=calcular_integral)
    calcular_boton.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana, text="Resultado:")
    resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

