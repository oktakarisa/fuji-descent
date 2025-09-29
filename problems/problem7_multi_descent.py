# problem7_multi_descent.py
#
# Problem 7: Visualize descent paths from multiple initial points
#

import numpy as np
import matplotlib.pyplot as plt
from problems.problem6_initial_values import descent_from_any_point

def visualize_multi_descent(fuji, start_points, alpha=0.2):
    """
    Visualize descent paths for multiple initial points.
    """
    all_paths = descent_from_any_point(fuji, start_points, alpha)

    plt.figure(figsize=(12, 6))
    for sp, path in all_paths.items():
        elevations = [fuji[p, 3] for p in path]  # column 3 = elevation
        plt.plot(path, elevations, marker='o', label=f'Start {sp}')
    
    plt.title("Descent Paths from Multiple Initial Points")
    plt.xlabel("Point Index")
    plt.ylabel("Elevation (m)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save plot
    plt.savefig("plots/multi_descent_paths.png")
    plt.close()
    print("✅ Problem 7: Multi-descent visualization saved to plots/multi_descent_paths.png")

def main():
    fuji = np.loadtxt("mtfuji_data.csv", delimiter=",", skiprows=1)
    start_points = [136, 142, 150, 160, 170]  # example initial points
    visualize_multi_descent(fuji, start_points, alpha=0.2)

if __name__ == "__main__":
    main()
