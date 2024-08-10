def num_trailing_zeros(N):
    zeros = 0
    while N > 0:
        N //= 5
        zeros += N
    return zeros

N = int(input())
print(num_trailing_zeros(N))