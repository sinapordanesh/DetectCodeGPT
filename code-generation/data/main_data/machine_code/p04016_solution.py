def f(b, n):
    if n < b:
        return n
    return f(b, n // b) + (n % b)

def find_b(n, s):
    for b in range(2, n):
        if f(b, n) == s:
            return b
    return -1

n, s = map(int, input().split())
print(find_b(n, s))