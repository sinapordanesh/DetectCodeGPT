X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = int(1e+9) + 7
def extgcd(a, b):
  if b == 0:
    return 1, 0
  else:
    x, y, u, v, k, l = 1, 0, 0, 1, a, b
    while l != 0:
      x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
      k, l = l, k % l
    return x
def inved(x):
  a = extgcd(x, mod)
  return a % mod

F = [
  [
    [1, 0, 0, Y[5]-Y[4]+1, 0], 
    [-1, 0, 0, 0, 0]
  ],
  [
    [1, X[5]-X[4]+1, 0, 0, 0], 
    [-1, 0, 0, X[5]-X[4]+1, 0]
  ],
  [
    [1, 0, 0, Y[3]-Y[2]+1, 0], 
    [-1, 0, 0, 0, Y[3]-Y[2]+1]
  ],
  [
    [1, 0, X[3]-X[2]+1, X[3]-X[2]+1, 0], 
    [-1, X[3]-X[2]+1, 0, 0, X[3]-X[2]+1]
  ],
  [
    [1, 0, 0, 0, Y[1]-Y[0]+1], 
    [-1, 0, 0, 0, 0]
  ],
  [
    [1, 0, 0, 0, X[1]-X[0]+1],
    [-1, 0, X[1]-X[0]+1, 0, 0]
  ],
  [
    [1, X[2]-X[5]-1, X[0]-X[3]-1, X[4]+Y[4]-X[3]-Y[3], X[2]+Y[2]-X[1]-Y[1]]
  ]
]
fact = [1 for i in range(2000001)]
invf = [0 for i in range(2000001)]
for i in range(2000000):
  fact[i+1] = ((i+1) * fact[i]) % mod
invf[-1] = inved(fact[2000000])
for i in range(2000000, 0, -1):
  invf[i-1] = (invf[i] * i) % mod
def encryptic(left, mat):
  cont = []
  for i in range(len(left)):
    for j in range(len(mat)):
      tmp = [left[i][0] * mat[j][0]]
      for k in range(1, 5):
        tmp.append(left[i][k] + mat[j][k])
      cont.append(tmp)
  return cont
Poly = [[1, 0, 0, 0, 0]]
for p in F:
  Poly = encryptic(p, Poly)
S = 0
D = {}
for p in Poly:
  a, b, c, d = -p[1], -p[2], p[3], p[4]
  s = p[0]
  M = min(b, c-a-2)
  tmp = 0
  for i in range(M+1):
    pix = (i+1) * invf[2+i+a] * invf[c-i-a-2]
    pix *= invf[b-i] * invf[d+i-b]
    pix %= mod
    tmp += pix
    tmp %= mod
  tmp *= fact[c] * fact[d]
  tmp %= mod
  S += s * tmp
  S %= mod
print(S)