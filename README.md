# Linear Programming Solver

A lightweight Python CLI for solving linear programming problems with two modes:

- graphical solution for 2-variable problems
- simplex optimization for higher-dimensional problems using SciPy

## Overview

This repository contains a small educational solver that chooses the appropriate solution method based on user input.
For 2 variables, it computes constraint intersections, filters feasible points, evaluates the objective, and plots the feasible region.
For more than 2 variables, it solves the problem using SciPy's `linprog` optimizer.

## Features

- CLI-driven solver in `main.py`
- 2-variable graphical method with constraint plotting
- Simplex method using `scipy.optimize.linprog`
- Automatic non-negativity bounds for all variables
- Prints intersection points, feasible corner points, and optimal results

## Architecture

- `main.py` — entry point and user interaction
- `main_graphical_method.py` — collects 2-variable problem input and controls the graphical solver flow
- `Utility_Func.py` — core helper routines for intersections, feasibility filtering, objective evaluation, and plotting

## Tech Stack

- Python 3
- NumPy
- Matplotlib
- SciPy

## Installation

Install required dependencies:

```bash
pip install numpy matplotlib scipy
```

## Usage

Run the solver from the repository root:

```bash
python main.py
```

Follow the prompts:

1. Enter the number of variables.
2. For 2 variables, enter objective coefficients and each constraint in `ax + by <= c` form.
3. For more than 2 variables, enter objective coefficients and each constraint coefficients followed by the RHS constant.

### Example CLI flow for 2 variables

```text
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

### Example CLI flow for simplex method

```text
Enter number of variables: 3
Enter objective function coefficients (Max Z = ax + by + cz + ...)
Enter coefficients separated by space: 4 3 5
Enter number of constraints:
2
Enter constraints in form: a1 a2 a3 ... <= b
Constraint 1: 2 1 1 20
Constraint 2: 1 3 2 30
```

## Project Structure

```text
main.py
main_graphical_method.py
Utility_Func.py
README.md
.vscode/settings.json
```

## Limitations

- Graphical solver supports only 2 variables and only `<=` constraints.
- Simplex solver accepts only inequality constraints in standard form with implicit non-negativity (`x >= 0`).
- The project does not support `>=` or equality constraints directly.
- There is no automated test suite included.
- No Docker, web API, or database integration is included.

## Future Improvements

- Add parsing for mixed inequality types (`>=`, `=`)
- Support variable bounds beyond implicit non-negativity
- Add unit tests and validation for user input
- Improve plotting to scale dynamically and overlay feasible region more robustly
- Add a configuration or file-based input mode

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with improvements.

## License

This repository does not include a license file. Use and modify at your own risk.
