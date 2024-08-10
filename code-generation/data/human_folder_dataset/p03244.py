N = int(input())
V = list(map(int,input().split()))

from collections import Counter

def get_counter(X):
  counter = Counter(X)
  X = counter.most_common()
  X.append((0,0))
  return X

V1 = get_counter(V[::2])
V2 = get_counter(V[1::2])

if V1[0][0] != V2[0][0]:
  print(N - (V1[0][1] + V2[0][1]))
else:
  print(N - max(V1[0][1] + V2[1][1],V1[1][1] + V2[0][1]))
