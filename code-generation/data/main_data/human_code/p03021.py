import sys;sys.setrecursionlimit(9**9);n=int(input());s=list(map(int,list(input())));e=[[]for _ in[0]*n]
for _ in[0]*(n-1):a,b=map(int,input().split());e[a-1].append(b-1);e[b-1].append(a-1)
def f(a):
  l,r,c=a[0]
  for u,v,d in a[1:]:l,r=max(max(l,u)-min(r,v),(l^u)&1),r+v;c+=d
  return[l,r,c]
def g(o,u):
  if(o!=u)&(len(e[u])==1):return[s[u]]*3
  l,r,c=f([g(u,v)for v in e[u]if o-v]);c+=s[u];return[l+c,r+c,c]
a=[r-c for l,r,c in[g(i,i)for i in range(n)]if l==c];print(min(a)//2if a else-1)