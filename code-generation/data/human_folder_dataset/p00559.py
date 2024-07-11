N, Q, S, T = map(int, input().split())
A = [int(input()) for i in range(N+1)]
C = 0
for i in range(N):
    if A[i] < A[i+1]:
        C += S * (A[i] - A[i+1])
    else:
        C += T * (A[i] - A[i+1])
def add(k, x):
    if x >= 0:
        if B[k] <= 0:
            if B[k] + x <= 0:
                return - T * x
            return T * B[k] - S * (B[k] + x)
        return - S * x
    if B[k] >= 0:
        if B[k] + x >= 0:
            return - S * x
        return S * B[k] - T * (B[k] + x)
    return - T * x

B = [A[i+1] - A[i] for i in range(N)]
ans = []
for q in range(Q):
    l, r, x = map(int, input().split())
    C += add(l-1, x); B[l-1] += x
    if r < N:
        C += add(r, -x); B[r] -= x
    ans.append(C)
print(*ans, sep='\n')
