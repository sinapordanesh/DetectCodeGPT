def max_remainder_sum(N):
    if N % 4 == 0:
        return N // 2 * (N // 2 - 1)
    elif N % 4 == 1 or N % 4 == 2:
        return N - 1
    else:
        return N // 2 * (N // 2 - 1)

N = int(input())
print(max_remainder_sum(N))