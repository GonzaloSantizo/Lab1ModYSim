import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def graficar_campo_direccion(f, x_min, x_max, y_min, y_max, x_step=0.2, y_step=0.2, unitario=False, lineas_flujo=False):
    """
    Grafica el campo de dirección de una ecuación diferencial dy/dx = f(x, y).

    Args:
        f: Función que define la ecuación diferencial.
        x_min, x_max: Límites del eje x.
        y_min, y_max: Límites del eje y.
        x_step, y_step: Pasos para la grilla de puntos.
        unitario: Si es True, grafica el campo unitario.
        lineas_flujo: Si es True, grafica algunas líneas de flujo.
    """

    # Crear la grilla de puntos
    x = np.arange(x_min, x_max + x_step, x_step)
    y = np.arange(y_min, y_max + y_step, y_step)
    X, Y = np.meshgrid(x, y)

    # Calcular las pendientes (dy/dx) en cada punto
    U = 1  # Componente x del vector
    V = f(X, Y)  # Componente y del vector

    # Normalizar los vectores si se solicita el campo unitario
    if unitario:
        norm = np.sqrt(U**2 + V**2)
        U /= norm
        V /= norm

    # Graficar el campo de dirección
    plt.figure(figsize=(8, 6))
    plt.quiver(X, Y, U, V, angles='xy')

    # Graficar algunas líneas de flujo si se solicita
    if lineas_flujo:
        for y_init in np.linspace(y_min, y_max, 10):
            x_span = (x_min, x_max)
            sol = odeint(f, y_init, x_span)
            plt.plot(x_span, sol, 'b-', linewidth=1)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Campo de Dirección')
    plt.grid(True)
    plt.show()

# Ejemplo 1: dy/dx = x + y
def f1(x, y):
    return x + y

graficar_campo_direccion(f1, -3, 3, -3, 3, lineas_flujo=True)

# Ejemplo 2: dy/dx = -y/x (campo unitario)
def f2(x, y):
    return -y / x

graficar_campo_direccion(f2, -3, 3, -3, 3, unitario=True)
