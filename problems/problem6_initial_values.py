# problem6_initial_values.py
#
# Problem 6: Descent from any initial point (humanized, concise output)
#

import numpy as np
from problems.problem4_descent import descend

def descent_from_any_point(fuji, start_points, alpha=0.2):
    """
    Run the descent simulation from multiple starting points.
    """
    results = {}
    for sp in start_points:
        path = descend(fuji, start=sp, alpha=alpha)
        results[sp] = path
    return results

def main():
    fuji = np.loadtxt("mtfuji_data.csv", delimiter=",", skiprows=1)
    
    # Only a few starting points for demo
    start_points = [136, 142, 150, 160, 170]
    all_paths = descent_from_any_point(fuji, start_points, alpha=0.2)
    
    print("Running Problem 6: Initial Values Experiment\n")
    for sp, path in all_paths.items():
        # Show first 5 + last 2 points for brevity
        if len(path) > 7:
            display_path = path[:5] + ["..."] + path[-2:]
        else:
            display_path = path
        print(f"Start {sp}: Path {display_path} | Total steps: {len(path)}")
    print("\n✅ Problem 6 completed.")

if __name__ == "__main__":
    main()
