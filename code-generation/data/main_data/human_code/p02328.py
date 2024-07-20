import sys, collections
file = sys.stdin
n = int(file.readline())
C = list(map(int, file.readline().split()))

def square(P):
    G = []
    L = collections.deque()
    for i,v in enumerate(P):
        if not L:
            L.append((i, v))
            continue
        if v > L[-1][1]:
            L.append((i, v))
        elif v < L[-1][1]:
            k = i - 1
            while L and v < L[-1][1]:
                a = L.pop()
                G.append((k - a[0] + 1) * a[1])
            L.append((a[0], v))
    while L:
        a = L.pop()
        G.append((len(P) - a[0]) * a[1])
    return max(G)

print(square(C))