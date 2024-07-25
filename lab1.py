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
        for y_init in np.linspace(y_min, y_max, 10):
            x_span = np.linspace(x_min, x_max, 100)
            sol = odeint(lambda y, x: f(x, y), y_init, x_span)
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

# Ejemplo 3: dy/dx = x^2 - y
def f3(x, y):
    return x**2 - y

graficar_campo_direccion(f3, -3, 3, -3, 3, lineas_flujo=True)