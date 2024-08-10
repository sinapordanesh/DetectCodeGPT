import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()
    A = [LI() for _ in range(N)]

    ctr = [0] * N

    sp = [0] * (M+1)
    for i in range(N):
        sp[A[i][ctr[i]]] += 1
    ans = max(sp)

    for _ in range(M-1):
        mi = sp.index(max(sp))
        sp[mi] = -1
        for i in range(N):
            if A[i][ctr[i]] == mi:
                while sp[A[i][ctr[i]]] < 0:
                    ctr[i] += 1
                sp[A[i][ctr[i]]] += 1
        ans = min(ans,max(sp))

    print(ans)


if __name__ == '__main__':
    main()