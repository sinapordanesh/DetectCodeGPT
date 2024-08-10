from collections import defaultdict

def gen(N, S, W):
    g = S
    for i in range(N):
        yield (g//7) % 10
        if g % 2 == 0:
            g //= 2
        else:
            g = (g//2) ^ W

def solve():
    N, S, W, Q = map(int, input().split())
    if N == 0:
        return False
    bs = list(gen(N, S, W))
    ans = 0
    if Q == 2 or Q == 5:
        cnt = 0
        for i in range(N):
            b = bs[i]
            if b != 0:
                cnt += 1
            if b % Q == 0:
                ans += cnt
    else:
        rev10 = pow(10, Q-2, Q)
        D = defaultdict(int)
        D[0] = 1
        s = 0; v = 1
        first = 1
        for i in range(N):
            b = bs[i]
            if first and b == 0:
                continue
            s = (s + v * b) % Q
            v = v * rev10 % Q
            ans += D[s]
            if i < N-1 and bs[i+1] != 0:
                D[s] += 1
            first = 0
    print(ans)
    return True

while solve():
    ...
