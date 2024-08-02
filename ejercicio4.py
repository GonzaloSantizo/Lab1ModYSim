import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def graficar_campo_direccion(f, x_min, x_max, y_min, y_max, lineas_flujo=False, unitario=False):
    x = np.linspace(x_min, x_max, 20)
    y = np.linspace(y_min, y_max, 20)
    X, Y = np.meshgrid(x, y)
    U = np.ones_like(X)
    V = f(X, Y)

    plt.quiver(X, Y, U, V, angles='xy')

    if lineas_flujo:
        for y_init in np.linspace(y_min, y_max, 1):
            x_span = np.linspace(x_min, x_max, 100)
            sol = odeint(lambda y, x: f(x, y), y_init, x_span)
            plt.plot(x_span, sol, 'b-', linewidth=1)


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Campo de Dirección')
    plt.grid(True)
    plt.show()

# Definimos la función de la EDO (la tuya)
def f(x, y):
    numerador = x - 3*y - 3*(x**2 - y**2) + 3*x*y
    denominador = 2*x - y + 3*(x**2 - y**2) + 2*x*y
    return numerador / denominador

# Graficamos el campo de direcciones con límites ajustados
graficar_campo_direccion(f, 0, 3, -1, 1, lineas_flujo=True) 
