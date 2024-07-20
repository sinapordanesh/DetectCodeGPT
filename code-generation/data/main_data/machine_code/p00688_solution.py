def factorization_quadratic_formula():
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        for p in range(1, 10001):
            if a % p != 0:
                continue
            for q in range(-10000, 10001):
                for r in range(1, 10001):
                    if c % r != 0:
                        continue
                    s = c // r
                    if r * s != c:
                        continue
                    if p * s + q * r == b and p * r == a:
                        print(p, q, r, s)
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            print("Impossible")

factorization_quadratic_formula()