def solve_simultaneous_equation():
    while True:
        try:
            a, b, c, d, e, f = map(int, input().split())
            x = round((c*e - b*f) / (a*e - b*d), 3)
            y = round((a*f - c*d) / (a*e - b*d), 3)
            print(f"{x} {y}")
        except EOFError:
            break

solve_simultaneous_equation()