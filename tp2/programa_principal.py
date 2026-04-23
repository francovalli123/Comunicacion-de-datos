import numpy as np
import matplotlib.pyplot as plt
import os

# Nota: para la realización del Script me he apoyado en IA por 
# falta de dominio total de las librerias usadas. 
# La IA se uso solamente como herramienta, no se abusó de su uso.

# -----------------------------
# Crear carpeta de salida
# -----------------------------
output_dir = "graficas_ej4"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------
# Función rectangular
# -----------------------------
def rect(t, t0, tau):
    return np.where(np.abs(t - t0) <= tau/2, 1, 0)

# -----------------------------
# Periodizacion
# -----------------------------
def periodic_signal(t, T, func):
    return func(np.mod(t, T))

# -----------------------------
# Los incisos del ejerciocio
# -----------------------------
incisos = {
    "a": {
        "T": 4,
        "xg": lambda t: rect(t, 1/4, 1/2)
    },
    "b": {
        "T": 4,
        "xg": lambda t: rect(t, 3/4, 1/2)
    },
    "c": {
        "T": 2,
        "xg": lambda t: rect(t, 1/4, 1/2)
    },
    "d": {
        "T": 2,
        "xg": lambda t: rect(t, 1/4, 1)
    },
    "e": {
        "T": 4,
        "xg": lambda t: rect(t, 1/4, 1/2) - rect(t, 3/4, 1/2)
    }
}

# -----------------------------
# Dominio temporal general
# -----------------------------
t = np.linspace(-5, 5, 2000)

# -----------------------------
# Loop principal
# -----------------------------
for nombre, params in incisos.items():
    
    T = params["T"]
    xg = params["xg"]

    # Señales
    xg_vals = xg(t)
    xp_vals = periodic_signal(t, T, xg)

    # -----------------------------
    # Energía (generadora)
    # -----------------------------
    dt = t[1] - t[0]
    energia = np.sum(xg_vals**2) * dt

    # -----------------------------
    # Potencia (periódica)
    # -----------------------------
    t_period = np.linspace(0, T, 2000)
    xp_period = periodic_signal(t_period, T, xg)
    dtp = t_period[1] - t_period[0]

    potencia = (1/T) * np.sum(xp_period**2) * dtp

    # -----------------------------
    # Mostrar resultados
    # -----------------------------
    print(f"\nInciso {nombre}:")
    print(f"Energía de xg(t): {energia:.4f}")
    print(f"Potencia de xp(t): {potencia:.4f}")

    # -----------------------------
    # Gráficas
    # -----------------------------
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, xg_vals)
    plt.title(f"Inciso {nombre} - Señal generadora xg(t)")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(t, xp_vals)
    plt.title(f"Inciso {nombre} - Señal periódica xp(t)")
    plt.grid()

    plt.tight_layout()

    # -----------------------------
    # Guardar imagen
    # -----------------------------
    filename = os.path.join(output_dir, f"inciso_{nombre}.png")
    plt.savefig(filename)
    plt.close()

print("\nTodas las gráficas fueron guardadas en la carpeta 'graficas_ej4'")