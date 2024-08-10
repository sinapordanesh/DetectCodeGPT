from collections import deque, defaultdict
import sys
def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N = int(readline())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a, b = map(int, readline().split()); a -= 1; b -= 1
        G[a].append(b)
        G[b].append(a)

    H = [-1]*N
    MOD = 10**9 + 9
    X1 = [0]*N; v1 = 13
    X2 = [0]*N; v2 = 17
    U = [0]*N
    que = deque([0])
    U[0] = 1
    D = [0]
    while que:
        v = que.popleft()
        for w in G[v]:
            if U[w]:
                continue
            U[w] = 1
            que.append(w)
            D.append(w)
    M = defaultdict(int)
    for v in reversed(D):
        h = 0
        su1 = su2 = 0
        for w in G[v]:
            if H[w] == -1:
                continue
            h = max(h, H[w])
            su1 += X1[w]; su2 += X2[w]
        H[v] = k = h+1
        X1[v] = w1 = (su1*v1 + 1) % MOD
        X2[v] = w2 = (su2*v2 + 1) % MOD
        M[k, w1, w2] += 1
    ans = 0
    for v in M.values():
        ans += v*(v-1)//2
    write("%d\n" % ans)
main()
