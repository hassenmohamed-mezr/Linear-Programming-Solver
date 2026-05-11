import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# =========================================
# Find intersection between two lines
# =========================================
def find_intersection(line1, line2):

    a1, b1, c1 = line1
    a2, b2, c2 = line2

    determinant = a1 * b2 - a2 * b1

    # Parallel lines
    if determinant == 0:
        return None

    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return (x, y)


# =========================================
# Get all intersections
# =========================================
def get_all_intersections(constraints):

    points = []

    n = len(constraints)

    for i in range(n):

        for j in range(i + 1, n):

            point = find_intersection(
                constraints[i],
                constraints[j]
            )

            if point is not None:
                points.append(point)

    return points


# =========================================
# Check if point satisfies all constraints
# =========================================
def is_feasible(point, constraints):

    x, y = point

    # Non-negativity constraints
    if x < 0 or y < 0:
        return False

    for a, b, c in constraints:

        if a * x + b * y > c + 1e-9:
            return False

    return True


# =========================================
# Filter feasible points only
# =========================================
def filter_feasible_points(points, constraints):

    feasible_points = []

    for point in points:

        if is_feasible(point, constraints):
            feasible_points.append(point)

    return feasible_points


# =========================================
# Calculate objective function value
# =========================================
def calculate_objective(point, a, b):

    x, y = point

    return a * x + b * y


# =========================================
# Find optimal point
# =========================================
def find_optimal_point(points, a, b):

    best_point = None
    best_value = float('-inf')

    for point in points:

        z = calculate_objective(point, a, b)

        if z > best_value:

            best_value = z
            best_point = point

    return best_point, best_value


# =========================================
# Plot constraints
# =========================================
def plot_constraints(constraints, feasible_points, best_point):

    x = np.linspace(0, 20, 400)

    plt.figure(figsize=(8, 8))

    for a1, b1, c1 in constraints:

        # Normal line
        if b1 != 0:

            y = (c1 - a1 * x) / b1

            plt.plot(
                x,
                y,
                label=f"{a1}x + {b1}y <= {c1}"
            )

        # Vertical line
        else:

            x_vertical = c1 / a1

            plt.axvline(
                x=x_vertical,
                label=f"{a1}x <= {c1}"
            )

    # Plot feasible points
    for point in feasible_points:

        plt.scatter(point[0], point[1])

        plt.text(
            point[0],
            point[1],
            f"({point[0]:.2f}, {point[1]:.2f})"
        )

    # Highlight optimal point
    if best_point is not None:

        plt.scatter(
            best_point[0],
            best_point[1],
            s=150,
            marker='*'
        )

        plt.text(
            best_point[0],
            best_point[1],
            " Optimal"
        )

    plt.xlim((0, 20))
    plt.ylim((0, 20))

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title("Graphical Method - Linear Programming")

    plt.grid()
    plt.legend()

    # =========================================
    # Shade feasible region
    # =========================================

    if len(feasible_points) > 2:

        import math

        # Calculate center point
        center_x = sum(p[0] for p in feasible_points) / len(feasible_points)
        center_y = sum(p[1] for p in feasible_points) / len(feasible_points)

        # Sort points circularly
        feasible_points.sort(
            key=lambda p: math.atan2(
                p[1] - center_y,
                p[0] - center_x
            )
        )

        # Create polygon
        polygon = Polygon(
            feasible_points,
            closed=True,
            alpha=0.3
        )

        # Add polygon to plot
        plt.gca().add_patch(polygon)


    plt.show()

    