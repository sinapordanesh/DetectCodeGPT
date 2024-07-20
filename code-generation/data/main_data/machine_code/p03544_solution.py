def lucas_number(N):
    if N == 0:
        return 2
    elif N == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, N+1):
            a, b = b, a + b
        return b

N = int(input())
print(lucas_number(N))