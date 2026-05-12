# Linear Programming Solver
# Project for DSS (Decision Support Systems)
# Author: Simple implementation for educational purposes

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from main_graphical_method import graphical_method
from main_Simplex_method import simplex_method



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