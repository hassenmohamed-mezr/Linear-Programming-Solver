# Linear Programming Solver

A simple Python project for solving Linear Programming (LP) problems using:

- Graphical Method (for 2 variables)
- Simplex Method using SciPy (for more than 2 variables)

## Features

- Detects number of variables automatically
- Uses graphical visualization for 2-variable problems
- Uses simplex optimization for larger problems
- Simple command-line interface
- Educational and beginner-friendly implementation

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- SciPy

---

## Installation

Install required libraries:

```bash
pip install numpy matplotlib scipy
```

---

## How to Run

```bash
python main.py
```

---

## Example

### Objective Function

Maximize:

Z = 4x + 3y + 5z

### Constraints

2x + y + z <= 20

x + 3y + 2z <= 30

2x + 2y + 3z <= 40

---

## Project Structure

```text
main.py
README.md
```

---

## Notes

- Graphical method works only for 2 variables.
- Simplex method is implemented using `scipy.optimize.linprog`.

---

## Author

DSS Course Project
