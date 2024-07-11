#coding:utf-8
n = int(input())
inf = 1000000000000000

def minHeapify(Q,i):
    H = len(Q)
    l = 2*i
    r = 2*i + 1
    if l < H and Q[l][1] < Q[i][1]:
        smallest = l
    else:
        smallest = i
    if r < H and Q[r][1] < Q[smallest][1]:
        smallest = r

    if smallest != i:
        Q[i], Q[smallest] = Q[smallest], Q[i]
        minHeapify(Q,smallest)

def buildMinHeap(Q):
    H = len(Q)
    for i in range(H // 2, -1, -1):
        minHeapify(Q,i)

def Insert(Q,key):
    v = key[0]
    Q.append([v,inf])
    lens = len(Q)
    heapIncreaseKey(Q,lens-1,key)

def heapIncreaseKey(Q,i,key):
    Q[i][1] = key[1]
    while i > 0 and Q[i // 2][1] > Q[i][1]:
        Q[i], Q[i // 2] = Q[i // 2], Q[i]
        i //= 2

def heapExtractMin(Q):
    H = len(Q)
    minv = Q[0][0]
    Q[0] = Q[H-1]
    Q.pop()
    minHeapify(Q,0)
    return minv




def dijkstra(s):
    color = ["white" for i in range(n)]
    d = [inf for i in range(n)]
    d[s] = 0
    Q = [[s,0]]
    while Q != []:
        u = heapExtractMin(Q)
        color[u] = "black"
        for vw in mtrx[u]:
            [v,w] = vw
            if color[v] != "black":
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    color[v] = "gray"
                    Insert(Q,[v,d[v]])
    return d



mtrx = [[] for i in range(n)]
for i in range(n):
    col = list(map(int,input().split()))
    u,k = col[0], col[1]
    for j in range(k):
        [v,w] = col[2*j+2: 2*j+4]
        mtrx[u].append([v,w])



d = dijkstra(0)
for i,j in enumerate(d):
    print(i,j)
