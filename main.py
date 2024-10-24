import numpy as np
import matplotlib.pyplot as plt

# Datos de la tabla
# Arranque
angle_v_iaux_arranque = 43.19  # grados
angle_v_imarcha_arranque = 34.55  # grados

# Régimen estacionario
angle_v_iaux_estacionario = 0  # grados
angle_v_imarcha_estacionario = 60.47  # grados

# Función para crear el diagrama fasorial
def plot_fasorial(title, angle_iaux, angle_imarcha, save_name):
    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Fasor de voltaje
    ax.quiver(0, 0, np.cos(0), np.sin(0), angles='xy', scale_units='xy', scale=1, color='blue', label='Voltaje (V)')
    
    # Fasor de IAUX
    ax.quiver(0, 0, np.cos(np.radians(angle_iaux)), np.sin(np.radians(angle_iaux)), angles='xy', scale_units='xy', scale=1, color='green', label=f'IAUX ({angle_iaux}°)')
    
    # Fasor de IMARCHA
    ax.quiver(0, 0, np.cos(np.radians(angle_imarcha)), np.sin(np.radians(angle_imarcha)), angles='xy', scale_units='xy', scale=1, color='red', label=f'IMARCHA ({angle_imarcha}°)')
    
    # Configuración de ejes y leyendas
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.set_xlabel('Eje Real')
    ax.set_ylabel('Eje Imaginario')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(f'/mnt/data/{save_name}')
    plt.show()

# Crear los diagramas fasoriales
plot_fasorial("Diagrama Fasorial - Estado de Arranque", angle_v_iaux_arranque, angle_v_imarcha_arranque, "fasorial_arranque.png")
plot_fasorial("Diagrama Fasorial - Estado Estacionario", angle_v_iaux_estacionario, angle_v_imarcha_estacionario, "fasorial_estacionario.png")
