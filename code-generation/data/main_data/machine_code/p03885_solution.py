import sys
input = sys.stdin.readline

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

MOD = 10**9 + 7

def count_pairs(C):
    count = 0
    for i in range(1 << N):
        A = [[0]*N for _ in range(N)]
        B = [[0]*N for _ in range(N)]
        for j in range(N):
            for k in range(N):
                if i >> (j+k) & 1:
                    A[j][k] = 1
                    B[j][k] = 1
        valid = True
        for j in range(N):
            for k in range(N):
                if sum(A[j][l]*B[l][k] for l in range(N)) % 2 != C[j][k]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            count += 1
    return count % MOD

print(count_pairs(C))