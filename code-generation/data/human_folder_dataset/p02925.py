import collections

def topological():
    """トポロジカルソート (有向グラフ) O(V+E)

    Vars:
        n (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]: iを始点に持つ辺の終点のリスト)
    
    Returns:
        list/bool: トポロジカル順序 (閉路が存在する場合はFalse)
    """
    in_degree = [0] * n
    for i in range(n):
        for v in edge[i]:
            in_degree[v] += 1
    
    nodelist = collections.deque()
    for i in range(n):
        if in_degree[i] == 0:
            nodelist.append(i)
    
    res = []
    while nodelist:
        p = nodelist.popleft()
        for q in edge[p]:
            in_degree[q] -= 1
            depth[q] = max(depth[q], depth[p] + 1)
            if in_degree[q] == 0:
                nodelist.append(q)
        
        res.append(p)
    
    if len(res) == n:
        return res
    else:
        return False


m = int(input())
a = [list(map(int, input().split())) for _ in range(m)]

n = m * (m - 1) // 2

num = 0
table = [[-1] * m for _ in range(m)]
for i in range(m):
    for j in range(i+1, m):
        table[i][j] = num
        table[j][i] = num
        num += 1

edge = [[] for _ in range(n)]
for i in range(m):
    for j in range(m-2):
        edge[table[i][a[i][j]-1]].append(table[i][a[i][j+1]-1])

depth = [0] * n
l = topological()

if not l:
    print(-1)
else:
    print(max(depth) + 1)