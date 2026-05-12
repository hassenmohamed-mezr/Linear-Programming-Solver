# Linear Programming Solver

A lightweight Python CLI tool for solving linear programming problems using two different methods:

- **Graphical Method**: For 2-variable problems, providing visual plots of the feasible region and optimal solution.
- **Simplex Method**: For problems with more than 2 variables, utilizing SciPy's optimization library for efficient computation.

## Overview

This project is an educational linear programming solver that automatically selects the appropriate solution method based on the number of variables entered by the user. It supports maximization problems with linear constraints and non-negativity bounds.

- For 2-variable problems: Computes constraint intersections, identifies feasible corner points, evaluates the objective function, and generates a plot of the feasible region with the optimal point highlighted.
- For higher-dimensional problems: Leverages SciPy's `linprog` function to solve the linear programming problem using the Simplex algorithm.

## Features

- Command-line interface (CLI) for easy interaction via `main.py`.
- Graphical visualization for 2-variable problems using Matplotlib.
- Robust Simplex implementation for multi-variable optimization.
- Automatic handling of non-negativity constraints for all variables.
- Detailed output including intersection points, feasible points, and optimal solution.
- Educational focus with clear step-by-step processing.

## Architecture

The project is organized into modular Python files for maintainability:

- `main.py`: Entry point handling user input and directing to the appropriate solving method.
- `main_graphical_method.py`: Manages input collection and flow for 2-variable graphical solutions.
- `main_Simplex_method.py`: Handles input and execution for Simplex method on problems with 3+ variables.
- `Utility_Func.py`: Contains core utility functions for constraint intersection calculations, feasibility checks, objective evaluation, and plotting.

## Tech Stack

- **Python 3**: Core programming language.
- **NumPy**: For numerical computations and array handling.
- **Matplotlib**: For generating plots in the graphical method.
- **SciPy**: Provides the `optimize.linprog` function for Simplex optimization.

## Installation

Ensure you have Python 3 installed. Install the required dependencies using pip:

```bash
pip install numpy matplotlib scipy
```

## Usage

Navigate to the project root directory and run the solver:

```bash
python main.py
```

Follow the interactive prompts:

1. Enter the number of variables (2 for graphical, 3+ for Simplex).
2. Provide objective function coefficients.
3. Specify the number of constraints and their coefficients.

### Example: 2-Variable Graphical Method

```
Enter number of variables: 2
Enter objective function:
Max Z = ax + by

a: 3
b: 2
Number of constraints: 2
Constraint 1
a1 (x coefficient): 1
b1 (y coefficient): 2
c: 8
Constraint 2
a1 (x coefficient): 2
b1 (y coefficient): 1
c: 10
```

This will generate a plot showing the feasible region and optimal point.

### Example: Simplex Method (3 Variables)

```
Enter number of variables: 3
Enter objective function coefficients (Max Z = ax + by + cz + ...)
Enter coefficients separated by space: 4 3 5
Enter number of constraints: 2
Enter constraints in form: a1 a2 a3 ... <= b
Constraint 1: 2 1 1 20
Constraint 2: 1 3 2 30
```

The solver will output the optimal solution using the Simplex algorithm.

## Project Structure

```
LP_Solver/
├── main.py                     # Main entry point
├── main_graphical_method.py    # Graphical method implementation
├── main_Simplex_method.py      # Simplex method implementation
├── Utility_Func.py             # Utility functions
└── README.md                   # This file
```

## Limitations

- Currently supports only maximization problems.
- Assumes all variables are non-negative (standard in many LP problems).
- Graphical method is limited to 2 variables for visualization purposes.
- Input validation is basic; ensure correct numerical inputs.

## Contributing

Feel free to submit issues or pull requests for improvements, bug fixes, or additional features.

## License

This project is open-source. Please refer to the license file if included.
