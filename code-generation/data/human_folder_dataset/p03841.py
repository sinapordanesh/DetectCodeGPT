def solve(X):
    N = len(X)
    X = sorted((x,i) for i,x in enumerate(X, start=1))
    L = N**2
    res = [-1]*L
    i = 0
    for x,n in X:
        r = n-1
        while r > 0 and i < x:
            if res[i] < 0:
                res[i] = n
                r -= 1
            i += 1
        if res[x] > 0 or r > 0:
            return None
        else:
            res[x] = n
    i = L
    for x,n in reversed(X):
        r = N-n
        while r > 0 and i > x:
            if res[i-1] < 0:
                res[i-1] = n
                r -= 1
            i -= 1
        if r > 0:
            return None

    return res

from itertools import permutations

def naive(X):
    N = len(X)
    for a in permutations(list(range(N))*N):

        for i,x in enumerate(X):
            if not (a[x] == i and sum(v==i for v in a[:x]) == i):
                break
        else:
            return [v+1 for v in a]
    return None

from random import shuffle

if __name__ == '__main__':

    # N = 3
    # for _ in range(1000):
    #     X = list(range(N**2))
    #     shuffle(X)
    #     X = X[:N]

    #     r1 = solve(X)
    #     r2 = naive(X)
    #     if (r1 is None) != (r2 is None):
    #         print(X)
    #         print(r1)
    #         print(r2)
    #         break

    N = int(input())
    X = [int(x)-1 for x in input().split()]
    r = solve(X)
    if r is None:
        print('No')
    else:
        print('Yes')
        print(*r)
