import numpy as np
import matplotlib.pyplot as plt
from ball import *

# Ruta de guardado
output_path = get_output_path("class4_figure1.png")

# Parámetros del límite
a = 3.6
b = 3.8
delta = 0.9
epsilon = 0.7

#x0 = a - delta + 2*delta / 3
#f0 = b - epsilon + 2*epsilon / 6

# Definir los puntos de interés
x_points = [0, a - delta,   a, a + delta]
y_points = [-0.5, b - epsilon,  b, b + epsilon]

# Interpolación polinómica
coeffs = np.polyfit(x_points, y_points, 3)
f_interp = np.poly1d(coeffs)

x_vals = np.linspace(-1, 5, 500)
f_vals = f_interp(x_vals)

x0 = a - 0.4
f0 = f_interp(x0)

# Estilo de ejes con flechas
rc = {"xtick.direction": "inout", "ytick.direction": "inout",
      "xtick.major.size": 5, "ytick.major.size": 5}

with plt.rc_context(rc):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Dibujar función
    ax.plot(x_vals, f_vals, color='red', linewidth=2)

    # Líneas verticales
    ax.plot([a - delta, a - delta], [0, b - epsilon], color='blue', linestyle='--')
    ax.plot([a + delta, a + delta], [0, b + epsilon], color='blue', linestyle='--')
    ax.plot([a , a ], [0, b], color='green', linestyle='--')
    ax.plot([x0 , x0 ], [0, f0], color='black', linestyle='--')
    ax.text(a - delta, -0.3, r"$a - \delta$", ha='center', fontsize=12)
    ax.text(a + delta, -0.3, r"$a + \delta$", ha='center', fontsize=12) 
    ax.text(a, -0.3, r"$a$", ha='center', fontsize=12) 
    ax.text(x0+0.1, 0.3, r"$x$", ha='center', fontsize=12) 

    # Líneas horizontales
    ax.plot([0, a - delta], [b - epsilon, b - epsilon], color='blue', linestyle='--')
    ax.plot([0, a + delta], [b + epsilon, b + epsilon], color='blue', linestyle='--')
    ax.plot([0, a], [b , b], color='green', linestyle='--')
    ax.plot([0, x0], [f0 , f0], color='black', linestyle='--')
    ax.text(-0.6, b - epsilon, r"$b - \varepsilon$", va='center', fontsize=12)
    ax.text(-0.6, b + epsilon, r"$b + \varepsilon$", va='center', fontsize=12) 
    ax.text(-0.4, b, r"$b$", va='center', fontsize=12)
    ax.text(-0.6, f0, r"$f(x)$", va='center', fontsize=12)

    # Punto f(x)
    ax.plot(a, b, 'o', color='red',  markerfacecolor='white')
    # Punto x
    ax.plot(a, b + 1.5, 'o', color='red')
    #ax.text(x, fx + 0.15, r"$f(x)$", fontsize=12)

    # Punto abierto (a, b)
    #ax.plot(a, b, marker='o', color='black', markersize=8, markerfacecolor='white')
    #ax.text(a + 0.05, b + 0.15, r"$(a, b)$", fontsize=12)

    # Líneas punteadas hacia (a, b)
    ax.vlines(a, ymin=b - 0.2, ymax=b, color='black', linestyle='dotted')
    ax.hlines(b, xmin=a - 0.2, xmax=a, color='black', linestyle='dotted')

    # Ejes estilo cartesiano
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Flechas en ejes
    ax.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", ms=10, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)

    # Ocultar números
    ax.set_xticks([])
    ax.set_yticks([])
 
    # Limites
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)

    # Guardar figura
    save_figure_at(fig, output_path)
