import matplotlib.pyplot as plt
import numpy as np
import os

# Path
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "..", "img")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "class2_figure1.png")

# Datos de la sucesión
xs = np.array([
    [0.2, 0.2], [0.4, 1.5], [0.8, 2], [1.2, 1.5], [1.6, 1.7],
    [1.9, 2.1], [2.1, 2.6], [2.7, 2.8], [3.1, 2.8], [3.3, 3], [3.3, 3.2]
])
labels = [
    "$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$",
    "$x_6$", "$x_7$", "$x_{k_0}$", "$x_{k_0+1}$", "$x_{k_0+2}$", "$x_{k_0+3}$"
]

centro = np.array([3.2, 3.0])
radio_epsilon = 0.7
fondo_color = "#ffffff"

fig, ax = plt.subplots(figsize=(6, 6), facecolor=fondo_color)
ax.set_facecolor(fondo_color)  # Fondo del área de dibujo

# Bola ε
ax.add_patch(plt.Circle(centro, radio_epsilon, color='orange', linestyle='--', fill=False, linewidth=2))

# Vector radio
arrow = centro - np.array([0.7, -0.1])
ax.annotate('', xy=arrow, xytext=centro,
            arrowprops=dict(facecolor='blue', shrink=0.01))

# Sucesión
ax.plot(xs[:,0], xs[:,1], 'o', color='red', markersize=6)
ax.plot(xs[:,0], xs[:,1], linestyle='dashed', color='gray')

# Etiquetas
for i, (x, y) in enumerate(xs):
    ax.text(x + 0.05, y + 0.05, labels[i], fontsize=10, color='blue')

ax.text(centro[0] - 0.45, centro[1] + 0.15, r"$\varepsilon$", color='orange', fontsize=14)

# Estética
ax.set_xlim(0, 4)
ax.set_ylim(0, 3.8)
ax.set_aspect('equal')
ax.axis('off')

# Guardar imagen con fondo incluido
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Imagen guardada correctamente en: {os.path.abspath(output_path)}")

plt.show()
