import math

n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

def library_number(x,n):
  l = list(range(1,n+1))
  tmp = 0
  for i in range(n):
    tmp += math.factorial(n-1-i)*l.index(x[i])
    l.remove(x[i])
  return tmp

ans = abs(library_number(p,n) - library_number(q,n))
print(ans)