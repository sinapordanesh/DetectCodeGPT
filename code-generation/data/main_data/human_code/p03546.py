import sys

def warshall_floyd():
    for k in range(10):
        for i in range(10):
            for j in range(10):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])

H, W = map(int, input().split())
inf = float("inf")
C = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(10)]
A = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(H)]
warshall_floyd()
res = 0
for row in A:
    for col in row:
        if col != -1:
            res += C[col][1]

print(res)
