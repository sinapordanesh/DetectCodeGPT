def nasu(a, j):
  return [-2*j, j * j + a]

def tami(x, ab):
  a, b = ab
  return a * x + b

def renritu(ab1, ab2):
  a1, b1 = ab1
  a2, b2 = ab2
  return (b2 - b1) / (a1 - a2)

def add(a, b):
  ab3 = nasu(a, b)
  while len(L) >= 2:
    ab1 = L[-2]
    ab2 = L[-1]
    x1 = renritu(ab1, ab2)
    x2 = renritu(ab2, ab3)
    if x1 > x2:
      L.pop()
    else:
      break
  L.append(ab3)

N, C = list(map(int, input().split()))
h = list(map(int, input().split()))

DP = [0] * N
L = [nasu(0, h[0])]

cnt = 0
for i in range(1, N):
  while cnt < len(L) - 1:
    x = tami(h[i], L[cnt])
    y = tami(h[i], L[cnt + 1])
    if x >= y:
      cnt += 1
    else:
      break
  DP[i] = h[i] ** 2 + C + tami(h[i], L[cnt])
  add(DP[i], h[i])

print(DP[-1])