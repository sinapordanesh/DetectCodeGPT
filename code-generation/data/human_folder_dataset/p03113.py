N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

def nasu(x, L):
  t = 1000
  a = -1
  for i in range(len(L)):
    if i == x: continue
    if L[i] < t:
      t = L[i]
      a = i
  return a

L = []
to = nasu(-1, a)
fr = -1
for i in range(K + 1):
  for j in range(N):
    if j == to: continue
    if j == fr: continue
    a[j] -= 1
    L.append(j + 1)
  if a[to] == 0:
    print(-1)
    exit()
  a[to] -= 1
  L.append(to + 1)
  fr = to
  to = nasu(to, a)

print(len(L))
for i in L:
  print(i, end = " ")
print("")