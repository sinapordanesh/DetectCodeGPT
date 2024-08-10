import sys
input = sys.stdin.readline

def min_spanning_tree(N, Q, queries):
    total_weight = 0
    for i in range(Q):
        A, B, C = queries[i]
        total_weight += C * ((A - B) % N)
    return total_weight

N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]
print(min_spanning_tree(N, Q, queries))