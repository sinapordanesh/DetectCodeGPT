N = int(input())
P = 998244353
A = [int(input()) for _ in range(N)]
s = sum(A)

def calc(m):
    X = [1] + [0] * s
    for a in A:
        for i in range(a, s+1)[::-1]:
            X[i] = (X[i] + X[i-a] * m) % P
    return X

Y = calc(2)
ans = sum([Y[i] for i in range(s//2+1)]) + (0 if s%2 else -calc(1)[s//2])
print((pow(3, N, P) - ans*3) % P)