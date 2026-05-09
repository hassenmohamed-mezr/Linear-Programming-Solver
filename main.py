# Linear Programming Solver
# Project for DSS (Decision Support Systems)
# Author: Simple implementation for educational purposes

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# -------------------------------
# Function: Graphical Method (2 variables only)
# -------------------------------
def graphical_method():
    print("\n--- Graphical Method Selected ---")

    # Objective function coefficients
    print("Enter objective function coefficients (Max Z = ax + by)")
    a = float(input("a: "))
    b = float(input("b: "))

    # For simplicity we assume 2 constraints in form:
    # ax + by <= c
    print("\nEnter constraints in form: ax + by <= c")

    constraints = []
    num_constraints = int(input("Number of constraints: "))

    for i in range(num_constraints):
        print(f"\nConstraint {i+1}")
        a1 = float(input("a1 (x coefficient): "))
        b1 = float(input("b1 (y coefficient): "))
        c1 = float(input("c: "))
        constraints.append((a1, b1, c1))

    # Generate x values
    x = np.linspace(0, 10, 400)

    plt.figure()

    # Plot constraints
    for a1, b1, c1 in constraints:
        if b1 != 0:
            y = (c1 - a1 * x) / b1
            plt.plot(x, y, label=f"{a1}x + {b1}y <= {c1}")

    plt.xlim((0, 10))
    plt.ylim((0, 10))

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Graphical Method - Feasible Region")
    plt.legend()
    plt.grid()

    print("\nPlotting constraints... close graph to continue.")
    plt.show()

    print("\nNote: Optimal solution estimation requires manual inspection in graphical method.")


# -------------------------------
# Function: Simplex Method
# -------------------------------
def simplex_method():
    print("\n--- Simplex Method Selected ---")

    # Objective function (maximize converted to minimize)
    print("Enter objective function coefficients (Max Z = ax + by + cz + ...)")
    c = list(map(float, input("Enter coefficients separated by space: ").split()))

    # Convert to minimization problem
    c = [-i for i in c]

    # Constraints
    print("\nEnter number of constraints:")
    m = int(input())

    A = []
    b = []

    print("\nEnter constraints in form: a1 a2 a3 ... <= b")

    for i in range(m):
        data = list(map(float, input(f"Constraint {i+1}: ").split()))
        A.append(data[:-1])
        b.append(data[-1])

    # Bounds (x >= 0)
    x_bounds = [(0, None) for _ in range(len(c))]

    # Solve using SciPy
    result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method="highs")

    print("\n--- Result ---")

    if result.success:
        print("Optimal Solution Found!")
        print("Values of variables:", result.x)
        print("Optimal Z value:", -result.fun)
    else:
        print("No solution found.")


# -------------------------------
# Main Program
# -------------------------------
def main():
    print("===================================")
    print(" Linear Programming Solver System")
    print("===================================\n")

    # Ask user number of variables
    n = int(input("Enter number of variables: "))

    if n == 2:
        graphical_method()
    else:
        simplex_method()


# Run program
if __name__ == "__main__":
    main()