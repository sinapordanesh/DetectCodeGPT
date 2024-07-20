def main(h,w,k,a):
  s=-1,-1
  for i in range(h):
    for j in range(w):
      if a[i][j]=='S':
        s=i,j
        break
    if s[0]!=-1:break
  inf=float('inf')
  da=[[inf]*w for _ in range(h)]
  da[s[0]][s[1]]=0
  todo=[s]
  dst=min(s[0],h-s[0]-1,s[1],w-s[1]-1)
  cnt=0
  while cnt<k and todo:
    ntodo=[]
    while todo:
      i,j=todo.pop()
      for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        if 0<=i+di<h and 0<=j+dj<w and a[i+di][j+dj]=='.' and da[i+di][j+dj]>da[i][j]+1:
          da[i+di][j+dj]=da[i][j]+1
          ntodo.append((i+di,j+dj))
          dst=min(dst,i+di,h-i-di-1,j+dj,w-j-dj-1)
    cnt+=1
    todo=ntodo
  return 1+(dst+k-1)//k

h,w,k=map(int,input().split())
a=[input() for _ in range(h)]
print(main(h,w,k,a))