import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,m = map(int,ipt().split())
    s = input()
    way = [[] for _ in range(n)]
    nway = [[0,0] for i in range(n)]
    for _ in range(m):
        a,b = map(int,ipt().split())
        a -= 1
        b -= 1
        way[a].append(b)
        way[b].append(a)
        if s[a] == "A":
            nway[b][0] += 1
        else:
            nway[b][1] += 1
        if s[b] == "A":
            nway[a][0] += 1
        else:
            nway[a][1] += 1
    al = [0]*n

    q = deque()
    for i,wi in enumerate(nway):
        if wi[0] == 0 or wi[1] == 0:
            q.append(i)

    while q:
        qi = q.pop()
        al[qi] = -1
        if s[qi] == "A":
            x = 0
        else:
            x = 1
        for i in way[qi]:
            if al[i] == 0:
                if nway[i][x] == 1:
                    q.append(i)
                else:
                    nway[i][x] -= 1

    if 0 in al:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
