import sys
sys.setrecursionlimit(10**7)

def main0(n,g,xyuv):
  # LCAを求める。自作する。
  # 各頂点の深さ。根は深さ0
  depth=[0]*n
  tour=[]
  hatsu=[0]*n
  dist=[0]*n
  tmp=0
  def et(p,v,tour,tmp,pc,pd):
    hatsu[v]=len(tour)-1
    for nv,c,d in g[v]:
      if nv==p:continue
      depth[nv]=depth[v]+1
      tmp+=d
      dist[nv]=tmp
      tour.append((nv,c,d))
      tour=et(v,nv,tour,tmp,c,d)
      tmp-=d
      tour.append((v,c,-d))
    return tour
  tour.append((0,0,0))
  tour=et(-1,0,tour,0,0,0)
  class SegmentTree():
    def __init__(self,size,f=lambda x,y:x+y,default=0):
      self.size=pow(2,(size-1).bit_length())
      self.f=f
      self.default=default
      self.data=[default]*(self.size*2)
    def update(self,i,x):
      i+=self.size
      self.data[i]=x
      while i:
        i>>=1
        self.data[i]=self.f(self.data[i*2],self.data[i*2+1])
    # 区間[l,r)へのクエリ
    def query(self,l,r):
      l,r=l+self.size,r+self.size
      lret,rret=self.default,self.default
      while l<r:
        if l&1:
          lret=self.f(self.data[l],lret)
          l+=1
        if r&1:
          r-=1
          rret=self.f(self.data[r],rret)
        l>>=1
        r>>=1
      return self.f(lret,rret)

  def func(x,y):
    if x[0]<y[0]:return x
    return y
  st=SegmentTree(len(tour),func,(n+1,0))
  for i,x in enumerate(tour):
    v=x[0]
    st.update(i,(depth[v],v))
  def lca(u,v):
    x,y=hatsu[u],hatsu[v]
    if x<y:
      y+=1
    else:
      x,y=y,x
      y+=1
    return st.query(x,y)[1]
  dc={}
  dcary={}
  for i,(v,c,d) in enumerate(tour):
    if c in dc:
      ci=1 if d>0 else -1
      dc[c].append((dc[c][-1][0]+ci,dc[c][-1][1]+d))
      dcary[c].append(i)
    else:
      dc[c]=[(0,0),(1,d)]
      dcary[c]=[0,i]
  ret=[]
  from bisect import bisect_right as bl
  for x,y,u,v in xyuv:
    u,v=u-1,v-1
    w=lca(u,v)
    uvlen=dist[u]+dist[v]-dist[w]*2
    if x not in dc:
      ret.append(uvlen)
      continue
    widx=bl(dcary[x],hatsu[w])-1
    wnum,wsum=dc[x][widx]
    uidx=bl(dcary[x],hatsu[u])-1
    vidx=bl(dcary[x],hatsu[v])-1
    unum,usum=dc[x][uidx]
    vnum,vsum=dc[x][vidx]
    uvsum=usum+vsum-wsum*2
    uvnum=unum+vnum-wnum*2
    #print(uvlen-uvsum+uvnum*y,uvlen,usum,vsum,wsum,uvnum,w)
    ret.append(uvlen-uvsum+uvnum*y)
  return ret

if __name__=='__main__':
  n,q=map(int,input().split())
  abcd=[list(map(int,input().split())) for _ in range(n-1)]
  xyuv=[list(map(int,input().split())) for _ in range(q)]
  g=[[] for _ in range(n)]
  for a,b,c,d in abcd:
    a,b=a-1,b-1
    g[a].append((b,c,d))
    g[b].append((a,c,d))
  ary0=main0(n,g,xyuv)
  print(*ary0,sep='\n')
