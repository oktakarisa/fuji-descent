# problem3_destination.py
#
# Problem 3: Function to calculate the destination point
#

import numpy as np
from problems.problem2_gradient import gradient_at_point

def next_point(fuji, current_point, alpha=0.2):
    """
    Calculate the next point index to move to based on gradient descent.

    Parameters
    ----------
    fuji : np.ndarray
        Fuji dataset with columns [point, lat, lon, elevation, distance].
    current_point : int
        Index of the current point.
    alpha : float, optional
        Learning rate (default=0.2).

    Returns
    -------
    int
        Destination point index.
    """
    g = gradient_at_point(fuji, current_point)
    destination = current_point - alpha * g
    destination = int(round(destination))

    # handle out-of-range cases
    if destination < 0:
        destination = 0
    elif destination >= len(fuji):
        destination = len(fuji) - 1

    return destination

def main():
    csv_path = "mtfuji_data.csv"
    fuji = np.loadtxt(csv_path, delimiter=",", skiprows=1)

    current = 136
    g = gradient_at_point(fuji, current)
    dest = next_point(fuji, current, alpha=0.2)

    print(f"Current point: {current}")
    print(f"Gradient: {g}")
    print(f"Next point: {dest}")

if __name__ == "__main__":
    main()
