from Utility_Func import (
    get_all_intersections,
    filter_feasible_points,
    calculate_objective,
    find_optimal_point,
    plot_constraints
)


# =========================================
# Main Graphical Method
# =========================================
def graphical_method():

    print("\n===================================")
    print(" GRAPHICAL METHOD")
    print("===================================")

    # =====================================
    # Objective Function
    # =====================================

    print("\nEnter objective function:")
    print("Max Z = ax + by")

    a = float(input("a: "))
    b = float(input("b: "))

    # =====================================
    # Constraints
    # =====================================

    print("\nEnter constraints in form:")
    print("ax + by <= c")

    constraints = []

    num_constraints = int(
        input("\nNumber of constraints: ")
    )

    for i in range(num_constraints):

        print(f"\nConstraint {i+1}")

        a1 = float(
            input("a1 (x coefficient): ")
        )

        b1 = float(
            input("b1 (y coefficient): ")
        )

        c1 = float(
            input("c: ")
        )

        constraints.append((a1, b1, c1))

    # =====================================
    # Add Non-Negativity Constraints
    # =====================================

    constraints.append((-1, 0, 0))
    constraints.append((0, -1, 0))

    # =====================================
    # Get Intersections
    # =====================================

    intersections = get_all_intersections(
        constraints
    )

    # =====================================
    # Filter Feasible Points
    # =====================================

    feasible_points = filter_feasible_points(
        intersections,
        constraints
    )

    # =====================================
    # Find Optimal Solution
    # =====================================

    best_point, best_value = find_optimal_point(
        feasible_points,
        a,
        b
    )

    # =====================================
    # Print Results
    # =====================================

    print("\n===================================")
    print(" INTERSECTION POINTS")
    print("===================================")

    for point in intersections:
        print(point)

    print("\n===================================")
    print(" FEASIBLE POINTS")
    print("===================================")

    for point in feasible_points:

        z = calculate_objective(
            point,
            a,
            b
        )

        print(
            f"Point: {point} ---> Z = {z}"
        )

    print("\n===================================")
    print(" OPTIMAL SOLUTION")
    print("===================================")

    if best_point is not None:

        print(f"Optimal Point: {best_point}")
        print(f"Maximum Z = {best_value}")

    else:

        print("No feasible solution found.")

    # =====================================
    # Plot
    # =====================================

    plot_constraints(
        constraints,
        feasible_points,
        best_point
    )

