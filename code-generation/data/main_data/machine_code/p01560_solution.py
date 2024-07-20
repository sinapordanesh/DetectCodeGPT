def expected_divisibles(n, m, a, p):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = 1
    for i in range(n):
        lcm = lcm * a[i] // gcd(lcm, a[i])

    ans = 0
    for i in range(1, lcm+1):
        prob = 1
        for j in range(n):
            prob *= 1 - p[j] / 100 if i % a[j] == 0 else p[j] / 100
        ans += i * (m // lcm) * prob

    return ans

n, m = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

print("{:.6f}".format(expected_divisibles(n, m, a, p)) )