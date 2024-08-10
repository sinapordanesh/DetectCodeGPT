def m():return map(int,input().split())
p,c=print,0
h,w,n=m()
l=[list(m())for i in range(n)]
l.sort()
for x,y in l:
 if y+c<x:exit(p(x-1))
 if y+c==x:c+=1
p(h)