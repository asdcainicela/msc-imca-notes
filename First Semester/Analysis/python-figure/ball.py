from types import SimpleNamespace  
import matplotlib.pyplot as plt
import numpy as np

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

def bola_abierta(ax, centro, radio, angulo_deg=45, radio_label=r"$\varepsilon$", radio_fontsize_label =20,
                 color_bola="orange", color_vector="blue",
                 color_radio_label="orange", color_centro="blue",
                 fill=False, fill_color="#ffe4b5",
                 centro_label=None, center_fontsize_label=18, centro_label_color="black"):
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

    # Etiqueta radial
    ax.text(centro[0] + 0.5 * desplazamiento[0],
            centro[1] + 0.6 * desplazamiento[1],
            radio_label, color=color_radio_label, fontsize= radio_fontsize_label )

    # Etiqueta del centro si se proporciona
    if centro_label:   
        displacement_factor = 0.1 if radio > 1 else 0.05   

        ax.text(
            centro[0] - displacement_factor * centro[0],  # Desplazamiento en el eje X
            centro[1] - displacement_factor * centro[1],  # Desplazamiento en el eje Y
            centro_label,  
            fontsize=center_fontsize_label,   
            color=centro_label_color 
        )


    return SimpleNamespace(
        centro=centro,
        radio=radio,
        angulo_deg=angulo_deg,
        desplazamiento=desplazamiento,
        borde=borde
    )
