def min_digits(N):
    min_val = float('inf')
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            A = i
            B = N // i
            min_val = min(min_val, max(len(str(A)), len(str(B))))
    return min_val

N = int(input())
print(min_digits(N))