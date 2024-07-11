N = int(input())
A = list(map(int, input().split()))

M = N * (N + 1) // 2
d, m = divmod(sum(A), M)

def no():
  print("NO")
  exit()

if m != 0:
  no()

cnt = 0
for i in range(N):
  t = A[i - 1] - A[i]
  t += d
  if t < 0:
    no()
  dd, mm = divmod(t, N)
  if mm != 0:
    no()
  cnt += dd

if cnt == d:
  print("YES")
else:
  no()