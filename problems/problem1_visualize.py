# problem1_visualize.py
#
# Problem 1: Visualize elevation data of Mt. Fuji
#
# Dataset (mtfuji_data.csv) has 5 columns:
#   0 -> Point number (index)
#   1 -> Latitude
#   2 -> Longitude
#   3 -> Elevation in meters   <-- this is what we plot on Y-axis
#   4 -> Distance from point 0
#
# We plot Point number (column 0) vs. Elevation (column 3)
# to see a cross-sectional view of Mt. Fuji.
#
# NOTE: Plots are saved to the "plots/" folder, not root.

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")  # use non-GUI backend to avoid segmentation faults
import matplotlib.pyplot as plt

def main():
    # Load the Mt. Fuji elevation data
    csv_path = "mtfuji_data.csv"
    np.set_printoptions(suppress=True)
    fuji = np.loadtxt(csv_path, delimiter=",", skiprows=1)

    # Extract columns: point index (x) and elevation (y)
    point_index = fuji[:, 0]   # column 0 = point number
    elevation = fuji[:, 3]     # column 3 = elevation in meters

    # Ensure "plots" directory exists
    os.makedirs("plots", exist_ok=True)

    # Plot the cross-section of Mt. Fuji
    plt.figure(figsize=(10, 6))  # figure size in inches (width, height)
    plt.plot(point_index, elevation, color="brown", linewidth=2)
    plt.title("Cross-sectional Elevation of Mt. Fuji", fontsize=14)
    plt.xlabel("Point Index")
    plt.ylabel("Elevation (m)")
    plt.grid(True, linestyle="--", alpha=0.6)

    # Save the plot into "plots" folder
    plot_path = os.path.join("plots", "fuji_cross_section.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"✅ Problem 1: Plot saved to {plot_path}")

# Allow standalone execution for debugging
if __name__ == "__main__":
    main()
