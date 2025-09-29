# main.py
"""
Main execution file for the Fuji Descent project.
Runs all problem scripts sequentially.
"""

from problems import (
    problem1_visualize,
    problem2_gradient,
    problem3_destination,
    problem4_descent,
    problem5_visualize_descent,
    problem6_initial_values,
    problem7_multi_descent,
    problem8_hyperparams,
)

def main():
    print("🚀 Starting Fuji Descent project...\n")

    print("Running Problem 1: Visualize Fuji Data")
    problem1_visualize.main()
    print("✅ Problem 1 completed.\n")

    print("Running Problem 2: Gradient Calculation")
    problem2_gradient.main()
    print("✅ Problem 2 completed.\n")

    print("Running Problem 3: Destination Check")
    problem3_destination.main()
    print("✅ Problem 3 completed.\n")

    print("Running Problem 4: Descent Simulation")
    problem4_descent.main()
    print("✅ Problem 4 completed.\n")

    print("Running Problem 5: Visualize Descent")
    problem5_visualize_descent.main()
    print("✅ Problem 5 completed.\n")

    print("Running Problem 6: Initial Values Experiment")
    problem6_initial_values.main()
    print("✅ Problem 6 completed.\n")

    print("Running Problem 7: Multi Descent Simulation")
    problem7_multi_descent.main()
    print("✅ Problem 7 completed.\n")

    print("Running Problem 8: Hyperparameter Tuning")
    problem8_hyperparams.main()
    print("✅ Problem 8 completed.\n")

    print("🎉 All problems executed successfully!")

if __name__ == "__main__":
    main()
