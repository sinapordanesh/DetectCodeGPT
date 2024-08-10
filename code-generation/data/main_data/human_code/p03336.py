def Z():
 m=-1;I=input;N,M,K=map(int,I().split());W=2000000;s=[0]*W;t=[0]*W;L=max(N,M)-1;R=range;p=lambda x:print(*reversed(x),sep='')
 for i,c in zip(R(N-1,m,m),I()):s[i]=int(c)
 for i,c in zip(R(M-1,m,m),I()):t[i]=int(c)
 for i in R(L,m,m):
  j=i;z=K
  while s[j]and t[j]and z:
   s[j]=t[j]=0;s[j+1]+=1;t[j+1]+=1;j+=1;z-=1;x=y=j
   while s[x]==2:s[x]=0;s[x+1]+=1;x+=1
   while t[y]==2:t[y]=0;t[y+1]+=1;y+=1
   j=max(x,y)
  L=max(L,j)
 s=s[:L+1];t=t[:L+1]
 while s[m]==0:s.pop()
 while t[m]==0:t.pop()
 p(s);p(t)
Z()