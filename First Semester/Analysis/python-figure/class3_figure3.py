import matplotlib.pyplot as plt
import numpy as np
import os 
from ball import *


#Colores
fondo_color     = "#ffffff"  # blanco limpio
#bola1
bola_color      = "#A0E8E0"  # celeste claro (bola 1)
vector_color    = "#0077B6"  # azul fuerte pero no oscuro
etiqueta_color  = "#0077B6"  # mismo que el vector
centro_color    = "#1B4965"  # azul marino (acentuar centro)
relleno_color   = "#D0F4F1"  # relleno celeste claro (muy suave)

# — Ruta de guardado —
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "..", "img")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "class3_figure3.png")

# — Figura —
fig, ax = plt.subplots(figsize=(6, 6), facecolor=fondo_color)
ax.set_facecolor(fondo_color)

# funcion ball
bola_a1=bola_abierta(
    ax,
    centro=np.array([2, 2]),
    radio=2,
    angulo_deg=145,
    radio_label = r"$\varepsilon_0$",
    radio_fontsize_label = 25, ## radio
    color_bola=bola_color,
    color_vector=vector_color,
    color_radio_label=etiqueta_color,
    color_centro=centro_color,
    fill=False,
    fill_color=relleno_color,
    centro_label=r"$a$",  
    center_fontsize_label = 25, 
    centro_label_color=centro_color  
)


# Ajustes generales
ax.set_xlim(-0.2, 4.2)
ax.set_ylim(-0.05, 4.1)
ax.set_aspect('equal')
ax.axis('off')

# Guardar
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Guardado en:", os.path.abspath(output_path))
plt.show()
