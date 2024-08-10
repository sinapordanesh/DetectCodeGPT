def minimum_amount(N, K, D):
    while True:
        if all(str(d) not in str(N) for d in D):
            return N
        N += 1

N, K = map(int, input().split())
D = list(map(int, input().split()))

print(minimum_amount(N, K, D))