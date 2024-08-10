import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    edge = [[] for _ in range(N+1)]
    cnt = [0] * (N+1)
    for i in range(2,N+1):
        u = NI()
        edge[i].append(u)
        cnt[u] += 1

    q = collections.deque()
    for i in range(2,N+1):
        if cnt[i] == 0:
            q.append((i,0))
            cnt[i] = 1


    out = [[] for _ in range(N+1)]
    ret = 0
    while q:
        u,d = q.popleft()
        out[u].append(d)
        if len(out[u]) == cnt[u]:
            out[u].sort(reverse=True)
            ret = 0
            for i,x in enumerate(out[u]):
                ret = max(ret,i+x+1)
            if u == 1: break
            for v in edge[u]:
                q.append((v,ret))


    print(ret-1)

if __name__ == '__main__':
    main()