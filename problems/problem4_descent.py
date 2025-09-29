# problem4_descent.py
#
# Problem 4: Function to simulate descending Mt. Fuji
#

import numpy as np
from problems.problem3_destination import next_point

def descend(fuji, start=136, alpha=0.2):
    """
    Simulate descent from a starting point using gradient descent logic.

    Parameters
    ----------
    fuji : np.ndarray
        Fuji dataset with columns [point, lat, lon, elevation, distance].
    start : int
        Starting point index (default: 136 near summit).
    alpha : float
        Learning rate / step size (default: 0.2).

    Returns
    -------
    list of int
        Sequence of visited point indices during descent.
    """
    path = [start]
    current = start
    MAX_STEPS = 500  # Safety cap to avoid infinite loops

    while True:
        nxt = next_point(fuji, current, alpha)
        if nxt == current or nxt < 0 or nxt >= len(fuji) or len(path) >= MAX_STEPS:
            break
        path.append(nxt)
        current = nxt

    return path

def main():
    fuji = np.loadtxt("mtfuji_data.csv", delimiter=",", skiprows=1)
    path = descend(fuji, start=136, alpha=0.2)
    print("Descent path (Problem 4):", path)

if __name__ == "__main__":
    main()
