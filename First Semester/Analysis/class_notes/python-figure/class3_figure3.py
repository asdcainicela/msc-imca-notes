import matplotlib.pyplot as plt
import numpy as np
import os 
from ball import *  # Importa todas las funciones de ball.py


# Definición de colores para diferentes bolas
colores_bola1 = {
    "bola_color": "#e63946",     # rojo armónico
    "vector_color": "#e59671",   # salmón claro
    "radio_label_color": "#FB8500", # naranja vivo
    "centro_color": "#219ebc",   # azul claro
    "relleno_color": "#FFE5B4",  # durazno suave
}

# — Ruta de guardado —
output_path = get_output_path("class3_figure3.png") 

radioScale = 1.1

fig, ax = crear_figura()  

# Bola Abierta
bola1 = ball(
    ax,
    centro=np.array([radioScale, radioScale]),
    radio=radioScale,
    tipo="abierta",  # explícitamente abierta
    forma="circulo", # especificamos círculo
    angulo_deg=135,
    radio_label=r"$\varepsilon_0$",
    radio_fontsize_label=25,
    color_bola=colores_bola1["bola_color"],
    color_vector=colores_bola1["vector_color"],
    color_radio_label=colores_bola1["radio_label_color"],
    color_centro=colores_bola1["centro_color"],
    fill=True,  # con relleno
    fill_color=colores_bola1["relleno_color"],
    centro_label=r"$a$",
    center_fontsize_label=40,
    centro_label_color=colores_bola1["centro_color"],
    grosor_circulo=4,  # grosor personalizado
    grosor_flecha=3    # grosor personalizado
)
# Ajustes generales
ax.set_xlim(-0.2, 2*radioScale+0.1)
ax.set_ylim(-0.05, 2*radioScale+0.1)
ax.set_aspect('equal')
ax.axis('off')

save_figure_at(fig, output_path) # Guardar