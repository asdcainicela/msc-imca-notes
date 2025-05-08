from types import SimpleNamespace
import matplotlib.pyplot as plt
import numpy as np
import os


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

def ball(ax, centro, radio, tipo="abierta", angulo_deg=45, 
         radio_label=r"$\varepsilon$", radio_fontsize_label=20,
         color_bola="orange", color_vector="blue",
         color_radio_label="orange", color_centro="blue",
         fill=False, fill_color="#ffe4b5",
         centro_label=None, center_fontsize_label=18, centro_label_color="black",
         grosor_circulo=2, grosor_flecha=1.5, forma="circulo"):
    
    # Determinar el estilo de línea basado en el tipo
    linestyle = '--' if tipo == "abierta" else '-'
    
    if forma == "circulo":
        # Bola circular
        circle = plt.Circle(
            centro, radio,
            edgecolor=color_bola,
            linestyle=linestyle,
            facecolor=fill_color if fill else 'none',
            linewidth=grosor_circulo,
            alpha=0.6 if fill else 1.0
        )
        ax.add_patch(circle)
    elif forma == "cuadrado":
        # Bola cuadrada (norma infinito)
        square = plt.Rectangle(
            (centro[0] - radio, centro[1] - radio),
            2 * radio, 2 * radio,
            edgecolor=color_bola,
            linestyle=linestyle,
            facecolor=fill_color if fill else 'none',
            linewidth=grosor_circulo,
            alpha=0.6 if fill else 1.0
        )
        ax.add_patch(square)
    elif forma == "diamante":
        # Bola diamante (norma 1)
        puntos_x = [centro[0], centro[0] + radio, centro[0], centro[0] - radio]
        puntos_y = [centro[1] + radio, centro[1], centro[1] - radio, centro[1]]
        diamond = plt.Polygon(list(zip(puntos_x, puntos_y)),
                            edgecolor=color_bola,
                            linestyle=linestyle,
                            facecolor=fill_color if fill else 'none',
                            linewidth=grosor_circulo,
                            alpha=0.6 if fill else 1.0)
        ax.add_patch(diamond)
    
    # Flecha radial
    angulo = np.radians(angulo_deg)
    desplazamiento = np.array([radio * np.cos(angulo), radio * np.sin(angulo)])
    borde = centro + desplazamiento
    ax.annotate('', xy=borde, xytext=centro,
                arrowprops=dict(arrowstyle='->', color=color_vector, lw=grosor_flecha))
    
    # Centro (bolita)
    ax.plot(*centro, marker='o', markersize=4, color=color_centro, zorder=5)
    
    # Etiqueta radial
    ax.text(centro[0] + 0.5 * desplazamiento[0],
            centro[1] + 0.6 * desplazamiento[1],
            radio_label, color=color_radio_label, fontsize=radio_fontsize_label)
    
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
        tipo=tipo,
        forma=forma,
        angulo_deg=angulo_deg,
        desplazamiento=desplazamiento,
        borde=borde
    )

# Mantener la función original para compatibilidad con código existente
def bola_abierta(ax, centro, radio, angulo_deg=45, radio_label=r"$\varepsilon$", radio_fontsize_label=20,
                 color_bola="orange", color_vector="blue",
                 color_radio_label="orange", color_centro="blue",
                 fill=False, fill_color="#ffe4b5",
                 centro_label=None, center_fontsize_label=18, centro_label_color="black"):
    
    # Llamar a la nueva función con parámetros por defecto para comportamiento de bola abierta
    return ball(
        ax=ax,
        centro=centro,
        radio=radio,
        tipo="abierta",
        angulo_deg=angulo_deg,
        radio_label=radio_label,
        radio_fontsize_label=radio_fontsize_label,
        color_bola=color_bola,
        color_vector=color_vector,
        color_radio_label=color_radio_label,
        color_centro=color_centro,
        fill=fill,
        fill_color=fill_color,
        centro_label=centro_label,
        center_fontsize_label=center_fontsize_label,
        centro_label_color=centro_label_color
    )

# Función para bola cerrada
def bola_cerrada(ax, centro, radio, angulo_deg=45, radio_label=r"$\varepsilon$", radio_fontsize_label=20,
                 color_bola="orange", color_vector="blue",
                 color_radio_label="orange", color_centro="blue",
                 fill=False, fill_color="#ffe4b5",
                 centro_label=None, center_fontsize_label=18, centro_label_color="black"):
    
    # Llamar a la nueva función con parámetros para comportamiento de bola cerrada
    return ball(
        ax=ax,
        centro=centro,
        radio=radio,
        tipo="cerrada",
        angulo_deg=angulo_deg,
        radio_label=radio_label,
        radio_fontsize_label=radio_fontsize_label,
        color_bola=color_bola,
        color_vector=color_vector,
        color_radio_label=color_radio_label,
        color_centro=color_centro,
        fill=fill,
        fill_color=fill_color,
        centro_label=centro_label,
        center_fontsize_label=center_fontsize_label,
        centro_label_color=centro_label_color
    )

def get_output_path(filename: str, subfolder: str = "img") -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", subfolder)
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)

def save_figure_at(fig, output_path: str, dpi: int = 300):
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor=fig.get_facecolor())
    print("Guardado en:", os.path.abspath(output_path))
    plt.show()

def crear_figura(color_fondo="#ffffff", tamaño=(6, 6)):
    """
    Crea una figura con color de fondo personalizado y tamaño especificado.
    
    Args:
        color_fondo (str): Color de fondo de la figura y del eje. Por defecto blanco (#ffffff).
        tamaño (tuple): Tamaño (ancho, alto) en pulgadas. Por defecto (6, 6).
        
    Returns:
        tuple: (fig, ax) de Matplotlib.
    """
    fig, ax = plt.subplots(figsize=tamaño, facecolor=color_fondo)
    ax.set_facecolor(color_fondo)
    return fig, ax