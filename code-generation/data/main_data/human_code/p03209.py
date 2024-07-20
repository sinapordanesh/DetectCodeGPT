n,x=map(int,input().split())

#lレベルバーガーの下からx層に含まれるパティーの数
a=[1]*(n+1)
p=[1]*(n+1)
for i in range(1,n+1):
  a[i]=a[i-1]*2+3
  p[i]=p[i-1]*2+1

def count(l,x):
  if l==0:
    if x>=1:
      return 1
    else:
      return 0
  else:
    if x==1:
      return 0
    elif x<a[l-1]+2:
      return count(l-1,x-1)
    elif x==a[l-1]+2:
      return p[l-1]+1
    elif a[l]>x:
      return count(l-1,x-a[l-1]-2)+p[l-1]+1
    else:
      return p[l]
    
print(count(n,x))    
    