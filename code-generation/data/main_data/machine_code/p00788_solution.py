def find_rational_numbers():
    while True:
        p, n = map(int, input().split())
        if p == 0 and n == 0:
            break

        for y in range(1, n+1):
            x = int((p * y * y) ** 0.5)
            if x * x == p * y * y:
                continue
            u = x - 1
            v = y
            if v <= n and u * u < p * v * v:
                break

        print(f"{x}/{y} {u}/{v}")

find_rational_numbers()