def find_happy_integer(D, N):
    if D == 0:
        return N if N != 100 else 101
    elif D == 1:
        return N * 100 if N != 100 else 10100
    elif D == 2:
        return N * 10000 if N != 100 else 1010000

D, N = map(int, input().split())
print(find_happy_integer(D, N))