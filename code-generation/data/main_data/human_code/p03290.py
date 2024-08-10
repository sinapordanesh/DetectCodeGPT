import sys
sys.setrecursionlimit(10 ** 6)

D,G=map(int,input().split())
p=[]
c=[]
for i in range(D):
  a,b=map(int,input().split())
  p += [a]
  c += [b]

def solve(bit):
  if bit >= (1<<D):
    return 1000
  p_sum=0
  num=0
  for i in range(D):
    if bit & (1<<i):
      p_sum += c[i] + p[i] * 100*(i+1)
      num += p[i]
  if p_sum >= G:
    return min(num,solve(bit+1))
  else:
    for i in reversed(range(D)):
      if bit & 1<<i:
        continue
      for j in range(p[i]):
        if p_sum >= G:
          break
        p_sum += 100*(i+1)
        num += 1
      else:
        return solve(bit+1)
    return min(num,solve(bit+1))

print(solve(0))