import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función que queremos integrar
funcion = x**2 + 3*x + 2  # Ejemplo de una función polinómica

# Calcular la integral indefinida
integral_indefinida = sp.integrate(funcion, x)
print(f"La integral indefinida es: {integral_indefinida}")

# Convertir la función simbólica en una función que podemos graficar
f_integral = sp.lambdify(x, integral_indefinida, "numpy")

# Crear los puntos para la gráfica
x_vals = np.linspace(-10, 10, 400)
y_vals = f_integral(x_vals)

# Graficar la integral indefinida
plt.plot(x_vals, y_vals, label=f'Integral de {funcion}')
plt.title("Gráfica de la Integral Indefinida")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
