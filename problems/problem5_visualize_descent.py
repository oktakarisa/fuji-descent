# problem5_visualize_descent.py
#
# Problem 5: Visualization of the descent process
#

import numpy as np
import matplotlib.pyplot as plt
from problems.problem4_descent import descend
from problems.problem2_gradient import gradient_at_point

def visualize_descent(fuji, alpha=0.2, start=136):
    """
    Visualize the descent process:
      - Cross-section of Mt. Fuji with descent path.
      - Altitude vs steps.
      - Slope vs steps.
    """

    # Run descent path
    path = descend(fuji, start=start, alpha=alpha)
    elevations = fuji[path, 3]
    slopes = [gradient_at_point(fuji, p) for p in path[:-1]]  # slope not defined at final stop
    steps = list(range(len(path)))

    # --- Plot 1: Cross-section with descent path ---
    plt.figure(figsize=(10, 5))
    plt.plot(fuji[:, 0], fuji[:, 3], label="Fuji cross-section")
    plt.scatter(path, elevations, color="red", label="Descent path")
    plt.xlabel("Point index")
    plt.ylabel("Elevation (m)")
    plt.title("Mt. Fuji Cross-Section with Descent Path")
    plt.legend()
    plt.savefig("plots/fuji_descent_path.png")
    plt.close()

    # --- Plot 2: Altitude vs Steps ---
    plt.figure(figsize=(8, 5))
    plt.plot(steps, elevations, marker="o", label="Altitude")
    plt.xlabel("Step")
    plt.ylabel("Elevation (m)")
    plt.title("Altitude Change During Descent")
    plt.legend()
    plt.savefig("plots/altitude_vs_steps.png")
    plt.close()

    # --- Plot 3: Slope vs Steps ---
    plt.figure(figsize=(8, 5))
    plt.plot(steps[:-1], slopes, marker="x", color="orange", label="Slope")
    plt.xlabel("Step")
    plt.ylabel("Slope (gradient)")
    plt.title("Slope Change During Descent")
    plt.legend()
    plt.savefig("plots/slope_vs_steps.png")
    plt.close()

def main():
    fuji = np.loadtxt("mtfuji_data.csv", delimiter=",", skiprows=1)
    visualize_descent(fuji, alpha=0.2, start=136)
    print("✅ Problem 5: Visualizations saved to plots/ folder.")

if __name__ == "__main__":
    main()
