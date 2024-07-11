import sys
input = sys.stdin.readline

L, N = map(int, input().split())
A = [int(input()) for _ in range(N)]

def solve(A):
    if len(A) == 1:
        return A[0]
    S = [None]*N
    s = 0
    for i, a in enumerate(A):
        s += a
        S[i] = s

    T = [None]*N
    t = 0
    for i in reversed(range(N)):
        t += (L-A[i])
        T[i] = t

    ans = 0
    for i in range(N-1):
        if 2*i+3 < N:
            ans = max(ans, 2*S[i]+2*(T[i+1]-T[2*i+3])-(L-A[i+1]))
        elif 2*i+2 > N:
            ans = max(ans, 2*(S[i]-S[2*i-N+1]) + 2*T[i+1] - (L-A[i+1]))
        else:
            ans = max(ans, 2*S[i]+2*T[i+1]-(L-A[i+1]))
    return ans

a1 = solve(A)
a2 = solve([L-a for a in reversed(A)])
print(max(a1, a2))