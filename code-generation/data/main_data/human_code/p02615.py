import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
N -= 2
ans = A[0]
A.pop(0)
if N % 2 == 0:
    for i in range(N//2):
        ans += A[i] * 2
else:
    for i in range(N//2):
        ans += A[i] * 2
    ans += A[N//2]

print(ans)