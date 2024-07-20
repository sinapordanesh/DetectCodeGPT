def divisible_by_2(N):
    if N % 2 == 0:
        return N
    else:
        return N - 1

N = int(input())
print(divisible_by_2(N))