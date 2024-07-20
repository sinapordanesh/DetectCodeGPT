N, A, B, C, D = list(map(int, input().split()))
M = N - 1
n = abs(A - B)
m = abs(C - D)

def prin(tf):
  if tf:
    print("YES")
  else:
    print("NO")
  exit()

if n > D * M:
  prin(False)

GC = n
GD = n
if M % 2 == 1:
  M -= 1
  GC = abs(n - C)
  GD = abs(n - D)
t = GC // (2 * C)
k = M // 2 - t
a = t * 2 * C
b = t * 2 * D + k * m

if b >= GD:
  prin(True)

if GD % (2 * D) == 0:
  prin(True)

t = GD // (2 * D) + 1
k = M // 2 - t
a = t * 2 * C - k * m
b = t * 2 * D


if a <= GC:
  prin(True)

prin(False)