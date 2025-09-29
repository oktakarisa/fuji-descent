# problem8_hyperparams.py
#
# Problem 8: Visualize effect of hyperparameter alpha on descent
#

import numpy as np
import matplotlib.pyplot as plt
from problems.problem4_descent import descend

def visualize_alpha_effect(fuji, start=136, alphas=[0.05, 0.2, 0.5, 0.8]):
    """
    Visualize descent paths with different alpha values.
    """
    plt.figure(figsize=(12, 6))

    for alpha in alphas:
        path = descend(fuji, start=start, alpha=alpha)
        elevations = [fuji[p, 3] for p in path]  # column 3 = elevation
        plt.plot(path, elevations, marker='o', label=f'α = {alpha}')

    plt.title(f"Descent Paths from Start {start} for Different α Values")
    plt.xlabel("Point Index")
    plt.ylabel("Elevation (m)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    plt.savefig("plots/hyperparam_alpha_descent.png")
    plt.close()
    print("✅ Problem 8: Hyperparameter visualization saved to plots/hyperparam_alpha_descent.png")

def main():
    fuji = np.loadtxt("mtfuji_data.csv", delimiter=",", skiprows=1)
    visualize_alpha_effect(fuji, start=136, alphas=[0.05, 0.2, 0.5, 0.8])

if __name__ == "__main__":
    main()
