def venn_diagram(U_W, U_H, A, B, A_intersection_B):
    import math

    def circle_center(circle_radius, x_min, y_min, x_max, y_max):
        x = circle_radius
        y = circle_radius

        if x < x_min:
            x = x_min
        elif x > x_max:
            x = x_max

        if y < y_min:
            y = y_min
        elif y > y_max:
            y = y_max

        return x, y

    def calculate_circle_radius(circle_area):
        return math.sqrt(circle_area / math.pi)

    def calculate_circle_area(radius):
        return math.pi * radius**2

    X_A = 0
    Y_A = 0
    R_A = calculate_circle_radius(A)
    X_B = 0
    Y_B = 0
    R_B = calculate_circle_radius(B)

    # Calculate the center of circle A
    X_A, Y_A = circle_center(R_A, R_A, R_A, U_W - R_A, U_H - R_A)

    # Calculate the center of circle B
    X_B, Y_B = circle_center(R_B, R_B, R_B, U_W - R_B, U_H - R_B)

    # Check if the circles stay inside the rectangle
    if X_A - R_A < -0.0001 or X_A + R_A > U_W + 0.0001 or Y_A - R_A < -0.0001 or Y_A + R_A > U_H + 0.0001 or X_B - R_B < -0.0001 or X_B + R_B > U_W + 0.0001 or Y_B - R_B < -0.0001 or Y_B + R_B > U_H + 0.0001:
        return "impossible"
    else:
        return f"{X_A} {Y_A} {R_A} {X_B} {Y_B} {R_B}"


# Sample Input
print(venn_diagram(10, 5, 1, 1, 0))
print(venn_diagram(10, 5, 2, 2, 1))
print(venn_diagram(10, 10, 70, 70, 20))