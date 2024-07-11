from pprint import *
N,K=map(int,input().split())
dpw=[[0 for _ in range(2*K+1)] for _ in range(2*K+1)]
dpb=[[0 for _ in range(2*K+1)] for _ in range(2*K+1)]
def getmatnum(x1,y1,x2,y2,mat):#左上を(x1,y1)右下を(x2,y2)にしてmatの中の左上~右下の領域の和をdpから算出
    if (x2==0)or(y2==0):
        return 0
    else:
        if (x1==-1):
            x1=0
        if (y1==-1):
            y1=0
        return mat[y2][x2]-mat[y1][x2]-mat[y2][x1]+mat[y1][x1]








for i in range(N):
    x,y,c=input().split()
    x=int(x)
    y=int(y)
    #print(x,y,c)
    if c=="W":
        dpw[(y%(2*K))+1][(x%(2*K))+1]=dpw[(y%(2*K))+1][(x%(2*K))+1]+1
    else:
        dpb[(y % (2*K))+1][(x % (2*K))+1] = dpb[(y % (2*K))+1][(x % (2*K))+1] + 1
#pprint(dpw)
#pprint(dpb)

for i in range(1,2*K+1):
    for j in range(1,2*K+1):
        dpb[i][j]=dpb[i][j-1]+dpb[i][j]

for i in range(1,2*K+1):
    for j in range(1,2*K+1):
        dpb[i][j]=dpb[i-1][j]+dpb[i][j]

for i in range(1,2*K+1):
    for j in range(1,2*K+1):
        dpw[i][j]=dpw[i][j-1]+dpw[i][j]

for i in range(1,2*K+1):
    for j in range(1,2*K+1):
        dpw[i][j]=dpw[i-1][j]+dpw[i][j]
ans=0
for i in range(K):
    for j in range(K):
        k=i+K
        l=j+K
        b1=getmatnum(-1,-1,i,j,dpb)+getmatnum(k,-1,2*K,j,dpb)+getmatnum(i,j,k,l,dpb)+getmatnum(-1,l,i,2*K,dpb)+getmatnum(k,l,2*K,2*K,dpb)
        w1=getmatnum(i,-1,k,j,dpw)+getmatnum(-1,j,i,l,dpw)+getmatnum(k,j,2*K,l,dpw)+getmatnum(i,l,k,2*K,dpw)
        b2=getmatnum(-1,-1,i,j,dpw)+getmatnum(k,-1,2*K,j,dpw)+getmatnum(i,j,k,l,dpw)+getmatnum(-1,l,i,2*K,dpw)+getmatnum(k,l,2*K,2*K,dpw)
        w2=getmatnum(i,-1,k,j,dpb)+getmatnum(-1,j,i,l,dpb)+getmatnum(k,j,2*K,l,dpb)+getmatnum(i,l,k,2*K,dpb)
        ans=max(ans,b1+w1,b2+w2)

        #print(i,j,k,l)
print(ans)
        #
#pprint(dpw)
#pprint(dpb)