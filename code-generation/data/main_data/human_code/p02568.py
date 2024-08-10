mod=998244353
mask=2**32
ide_ele=0
lazy_ele=mask
def segfunc(a,b):
  a1,a2=divmod(a,mask)
  b1,b2=divmod(b,mask)
  c1=(a1+b1)%mod
  c2=(a2+b2)
  return (c1*mask)+c2
def op(a,x):
  a1,a2=divmod(a,mask)
  x1,x2=divmod(x,mask)
  c1=(a1*x1+a2*x2)%mod
  c2=a2
  return (c1*mask)+c2
def merge(x,y):
  x1,x2=divmod(x,mask)
  y1,y2=divmod(y,mask)
  z1=(x1*y1)%mod
  z2=(x2*y1+y2)%mod
  return (z1*mask)+z2
class lazysegmenttree():
  def __init__(self,init_val,func=segfunc,ie=ide_ele,le=lazy_ele,op=op,merge=merge):
    n=len(init_val)
    self.func=func
    self.op=op
    self.merge=merge
    self.ie=ie
    self.le=le
    self.h=(n-1).bit_length()
    self.num=1<<self.h
    self.tree=[ie]*self.num*2
    self.lazy=[le]*self.num*2
    for i in range(n):
      self.tree[i+self.num]=init_val[i]
    for i in range(self.num-1,0,-1):
      self.tree[i]=func(self.tree[2*i],self.tree[2*i+1])
  def reflect(self,k):
    if self.lazy[k]==self.le:return self.tree[k]
    return self.op(self.tree[k],self.lazy[k])
  def propagate(self,k):
    if self.lazy[k]==self.le:return
    self.lazy[2*k]=self.merge(self.lazy[2*k],self.lazy[k])
    self.lazy[2*k+1]=self.merge(self.lazy[2*k+1],self.lazy[k])
    self.tree[k]=self.reflect(k)
    self.lazy[k]=self.le
  def thrust(self, k):
    for i in range(1,self.h+1)[::-1]:
      self.propagate(k>>i)
  def recalc(self,k):
    while k:
      k>>=1
      self.tree[k]=self.func(self.reflect(2*k),self.reflect(2*k+1))
  def update(self,left_0,right_0,value):
    l=left_0+self.num
    r=right_0+self.num+1
    vl=l
    vr=r
    x=value
    self.thrust(l)
    self.thrust(r-1)
    while r-l>0:
      if l&1:
        self.lazy[l]=self.merge(self.lazy[l],x)
        l+=1
      if r&1:
        r-=1
        self.lazy[r]=self.merge(self.lazy[r],x)
      l>>=1
      r>>=1
    self.recalc(vl)
    self.recalc(vr-1)
  def query(self,left_0,right_0):
    l=left_0+self.num
    r=right_0+self.num+1
    self.thrust(l)
    self.thrust(r-1)
    vl=vr=self.ie
    while r-l>0:
      if l&1:
        vl=self.func(vl,self.reflect(l))
        l+=1
      if r&1:
        r-=1
        vr=self.func(self.reflect(r),vr)
      l>>=1
      r>>=1
    return self.func(vl,vr)//mask
n,q=map(int,input().split())
a=[(i*mask)+1 for i in map(int,input().split())]
st=lazysegmenttree(a)
ans=[]
for _ in range(q):
  q,*p=map(int,input().split())
  if q:
    l,r=p
    ans+=[st.query(l,r-1)]
  else:
    l,r,b,c=p
    st.update(l,r-1,(b*mask)+c)
print(*ans,sep='\n')