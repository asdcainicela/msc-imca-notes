import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.interpolate import CubicSpline

# — Configuración tipográfica Palatino/MathPazo —
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Palatino'],
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Palatino',
    'mathtext.it': 'Palatino:italic',
    'mathtext.bf': 'Palatino:bold',
})

# — Rutas —
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "..", "img")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "class3_figure1.png")

# — Datos de la sucesión —
pts = np.array([
    [0.2, 0.2], [0.4, 1.5], [0.8, 2], [1.2, 1.5], [1.6, 1.7],
    [1.9, 2.1], [2.1, 2.6], [2.7, 2.8], [3.1, 2.8], [3.3, 3], [3.3, 3.2]
])
labels = [
    "$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$",
    "$x_6$", "$x_7$", "$x_{k_0}$", "$x_{k_0+1}$",
    "$x_{k_0+2}$", "$x_{k_0+3}$"
]
centro = np.array([3.2, 3.0])
radio_eps = 0.7
fondo = "#ffffff"

# — Parámetro t —
t = np.arange(len(pts))

# — Splines paramétricas —
cs_x = CubicSpline(t, pts[:,0], bc_type='natural')
cs_y = CubicSpline(t, pts[:,1], bc_type='natural')

# — Nuevo muestreo —
t_new = np.linspace(t.min(), t.max(), 500)
x_new = cs_x(t_new)
y_new = cs_y(t_new)

# — Dibujo —
fig, ax = plt.subplots(figsize=(6,6), facecolor=fondo)
ax.set_facecolor(fondo)

# Bola ε
ax.add_patch(plt.Circle(centro, radio_eps,
                        color='orange', linestyle='--',
                        fill=False, linewidth=2))

# Radio como flecha simple
arrow = centro - np.array([0.7, -0.1])
ax.annotate(
    '', 
    xy=arrow, 
    xytext=centro,
    arrowprops=dict(
        arrowstyle='->',
        color='blue',
        lw=1.5
    )
)

# Punto pequeño en el centro
ax.plot(centro[0], centro[1],
        marker='o',
        markersize=4,    # tamaño pequeño
        color='blue',
        zorder=5)        # para que quede encima de todo

# Curva suave en estilo dashed
ax.plot(x_new, y_new, linestyle='--', color='gray', linewidth=1)

# Puntos originales
ax.plot(pts[:,0], pts[:,1], 'o', color='red', markersize=6)

# Etiquetas
for i, (x,y) in enumerate(pts):
    ax.text(x+0.05, y+0.05, labels[i], fontsize=14, color='blue')
ax.text(centro[0]-0.45, centro[1]+0.15,
        r"$\varepsilon$", color='orange', fontsize=14)

# Ajustes finales
ax.set_xlim(0, 4)
ax.set_ylim(0, 3.8)
ax.set_aspect('equal')
ax.axis('off')

# Guardar con fondo
plt.savefig(output_path, dpi=300,
            bbox_inches='tight',
            facecolor=fig.get_facecolor())
print("Guardado en:", os.path.abspath(output_path))

plt.show()
