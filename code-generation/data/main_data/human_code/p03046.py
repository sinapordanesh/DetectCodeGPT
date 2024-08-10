def main(m,k): 
  if k==0:
    ary=[]
    for i in range(2**m):
      ary.append(i)
      ary.append(i)
    return ary
  elif k>=2**m or m==1:
    return [-1]
  else:
    mi=set(range(2**m))
    b=[]
    while mi:
      i=mi.pop()
      j=i^k
      mi.discard(j)
      u=mi.pop()
      v=u^k
      mi.discard(v)
      b.append((i,j,u,v))
    ary=[]
    for i,j,u,v in b:
      ary.append(i)
      ary.append(j)
      ary.append(u)
      ary.append(v)
      ary.append(j)
      ary.append(i)
      ary.append(v)
      ary.append(u)
    return ary

m,k=map(int,input().split())
ary=main(m,k)

print(*ary,sep=' ')
exit()
print(len(ary))