import matplotlib.pyplot as plt
import numpy as np
import os
from types import SimpleNamespace  

# — Tipografía estilo MathPazo —
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Palatino'],
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Palatino',
    'mathtext.it': 'Palatino:italic',
    'mathtext.bf': 'Palatino:bold',
})
#Colores
fondo_color     = "#ffffff"  # blanco limpio
#bola1
bola_color      = "#A0E8E0"  # celeste claro (bola 1)
vector_color    = "#0077B6"  # azul fuerte pero no oscuro
etiqueta_color  = "#0077B6"  # mismo que el vector
centro_color    = "#1B4965"  # azul marino (acentuar centro)
relleno_color   = "#D0F4F1"  # relleno celeste claro (muy suave)
#bola 2
bola_color2     = "#FFB703"  # naranja suave y vibrante
vector_color2   = "#FB8500"  # naranja más oscuro (contraste con celeste)
etiqueta_color2 = "#FB8500"  # igual que vector para cohesión
centro_color2   = "#9A031E"  # rojo profundo (acentuar el punto central)
relleno_color2  = "#FFE5B4"  # crema-naranja pastel

 


def bola_abierta(ax, centro, radio, angulo_deg=45, etiqueta=r"$\varepsilon$",
                 color_bola="orange", color_vector="blue",
                 color_etiqueta="orange", color_centro="blue",
                 fill=False, fill_color="#ffe4b5"):

    # Bola
    circle = plt.Circle(
        centro, radio,
        edgecolor=color_bola,
        linestyle='--',
        facecolor=fill_color if fill else 'none',
        linewidth=2,
        alpha=0.6 if fill else 1.0
    )
    ax.add_patch(circle)

    # Flecha radial
    angulo = np.radians(angulo_deg)
    desplazamiento = np.array([radio * np.cos(angulo), radio * np.sin(angulo)])
    borde = centro + desplazamiento
    ax.annotate('', xy=borde, xytext=centro,
                arrowprops=dict(arrowstyle='->', color=color_vector, lw=1.5))

    # Centro (bolita)
    ax.plot(*centro, marker='o', markersize=4, color=color_centro, zorder=5)

    # Etiqueta ε
    ax.text(centro[0] + 0.5 * desplazamiento[0],
            centro[1] + 0.6 * desplazamiento[1],
            etiqueta, color=color_etiqueta, fontsize=20)

    # ← Retorno útil para componer figuras
    return SimpleNamespace(
        centro=centro,
        radio=radio,
        angulo_deg=angulo_deg,
        desplazamiento=desplazamiento,
        borde=borde
    )

# — Ruta de guardado —
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "..", "img")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "class3_figure2.png")

# — Figura —
fig, ax = plt.subplots(figsize=(6, 6), facecolor=fondo_color)
ax.set_facecolor(fondo_color)

# Llamada
bola_a1=bola_abierta(
    ax,
    centro=np.array([2, 2]),
    radio=2,
    angulo_deg=45,
    etiqueta=r"$\varepsilon$",
    color_bola=bola_color,
    color_vector=vector_color,
    color_etiqueta=etiqueta_color,
    color_centro=centro_color,
    fill=True,
    fill_color=relleno_color
)

bola_a1=bola_abierta(
    ax,
    centro=bola_a1.centro+np.array([bola_a1.radio * np.cos(np.radians(100)), bola_a1.radio * np.sin(np.radians(100))]),
    radio=0.5,
    angulo_deg=145,
    etiqueta=r"$\delta$",
    color_bola=bola_color2,
    color_vector=vector_color2,
    color_etiqueta=etiqueta_color2,
    color_centro=centro_color2,
    fill=True,
    fill_color=relleno_color2
)

# Ajustes generales
ax.set_xlim(-0.2, 4.2)
ax.set_ylim(-0.2, 5)
ax.set_aspect('equal')
ax.axis('off')

# Guardar
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Guardado en:", os.path.abspath(output_path))
plt.show()
