# for change the recursion limit
import sys
sys.setrecursionlimit(10 ** 6)

# to enable variable use in global
global tree, point

# v : current node, f : parent node 
def dfs(v, f):
    for next_v in tree[v]:
        # parents node is already visited
        if next_v == f:
            continue
    
        point[next_v] += point[v]
        dfs(next_v, v)

n , q = map(int, input().split())
# initalize gloabal variables
tree = [[] for _ in range(n)]
point = [0] * n

for _ in range(n - 1):
    a , b = map(int,input().split())
    tree[b - 1].append(a - 1)
    tree[a - 1].append(b - 1)

for _ in range(q):
    p , x = map(int, input().split())
    point[p - 1] += x

dfs(0, 0)
print(*point)