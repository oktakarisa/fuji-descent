# problem2_gradient.py
#
# Problem 2: Function to calculate gradient at a given point
#

import numpy as np

def gradient_at_point(fuji, point):
    """
    Calculate the gradient (slope) at a given point.

    Parameters
    ----------
    fuji : np.ndarray
        Fuji dataset with columns [point, lat, lon, elevation, distance].
    point : int
        Index of the current point.

    Returns
    -------
    float
        Gradient at the given point.
    """
    if point <= 0 or point >= len(fuji):
        raise ValueError("Point must be within the range 1 to len(fuji)-1")

    x0, y0 = fuji[point - 1, 0], fuji[point - 1, 3]  # previous point
    x1, y1 = fuji[point, 0], fuji[point, 3]          # current point

    gradient = (y1 - y0) / (x1 - x0)
    return gradient

def main():
    csv_path = "mtfuji_data.csv"
    fuji = np.loadtxt(csv_path, delimiter=",", skiprows=1)

    # Example: calculate gradient at point 136 (near summit)
    g = gradient_at_point(fuji, 136)
    print(f"Gradient at point 136: {g}")

if __name__ == "__main__":
    main()
