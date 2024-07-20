def find_minimum_k(N):
    k = 1
    total = 1
    while total % N != 0:
        k += 1
        total += k
    return k

N = int(input())
print(find_minimum_k(N))