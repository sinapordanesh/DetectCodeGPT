def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n // b) + (n % b)

def find_b(n, s):
    if n == s:
        return n + 1
    for b in range(2, int(n ** 0.5) + 1):
        if f(b, n) == s:
            return b
    for p in range(int(n ** 0.5), 0, -1):
        if (n - s) % p == 0:
            b = (n - s) // p + 1
            if f(b, n) == s:
                return b
    return -1

n, s = map(int, input().split())
print(find_b(n, s))