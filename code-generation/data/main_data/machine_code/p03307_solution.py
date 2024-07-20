def min_divisible_by_2_and_N(N):
    if N % 2 == 0:
        return N
    else:
        return 2 * N

N = int(input())
print(min_divisible_by_2_and_N(N))