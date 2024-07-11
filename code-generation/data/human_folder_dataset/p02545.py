import sys
readline = sys.stdin.buffer.readline

class E:
	def __init__(self,to,nx):
		self.to=to
		self.nx=nx

class Graph:
	def __init__(self,n):
		self.n=n
		self.head=[None]*n
	
	def ae(self,a,b):
		head=self.head
		head[a]=E(b,head[a])
		#head[b]=E(a,head[b])
		return head[a]

def scc(g):
	n=g.n
	cur=g.head
	last=[None]*n
	order=[-1]*n
	low=[-1]*n
	bl=[-1]*n
	idx=[]
	st=[]
	num=0
	for i in range(n):
		if order[i]!=-1:
			continue
		rec=[i]
		while rec:
			v=rec[-1]
			if last[v] is None:
				#first in v
				
				order[v]=low[v]=num
				num+=1
				st.append(v)
			else:
				#process last edge
				
				low[v]=min(low[v],low[last[v].to])
			
			found=False
			while cur[v] is not None:
				#process next edge
				e=cur[v]
				cur[v]=e.nx
				to=e.to
				
				if order[to]==-1:
					#visit another node
					rec.append(to)
					last[v]=e
					found=True
					break
				elif bl[to]==-1:
					low[v]=min(low[v],order[to])
			
			if not found:
				#last out v
				rec.pop()
				
				if order[v]==low[v]:
					c=len(idx)
					tmp=[]
					while True:
						a=st.pop()
						bl[a]=c
						tmp.append(a)
						if v==a:
							break
					idx.append(tmp)

	s=len(idx)
	for i in range(n):
		bl[i]=s-1-bl[i]
	idx.reverse()
	
	return (s,bl,idx)

class twosat:
	def __init__(self,n):
		self.n=n
		self.g=Graph(2*n)
	
	def add(self,x,y):
		self.g.ae(x^1,y)
		self.g.ae(y^1,x)
	
	def solve(self):
		s,bl,idx=scc(self.g)
		for i in range(self.n):
			if bl[i*2]==bl[i*2+1]:
				return False
		return True

n=int(readline())
N=n*3
a=list(map(int,readline().split()))
b=list(map(int,readline().split()))

for i in range(N):
	a[i]-=1
	b[i]-=1

apos=[[] for i in range(n)]
for i in range(N):
	apos[a[i]].append(i)

bpos=[[] for i in range(n)]
for i in range(N):
	bpos[b[i]].append(i)

def feasible(l,r):
	t=[False]*N
	
	def issubseq():
		head=l
		for i in range(N):
			if t[i]:
				while head<r and a[i]!=b[head]:
					head+=1
				if head==r:
					return False
				head+=1
		return True
	
	l2r=[]
	r2l=[]
	w=[]
	for val in range(n):
		z=[]
		for x in bpos[val]:
			if x<l:
				z.append(0)
			elif x<r:
				z.append(1)
			else:
				z.append(2)
		
		if z==[0,0,0]:
			return False
		elif z==[0,0,1]:
			t[apos[val][2]]=1
		elif z==[0,0,2]:
			x=l-bpos[val][0]
			y=bpos[val][2]-r
			r2l.append((x,y))
		elif z==[0,1,1]:
			t[apos[val][0]]=1
			t[apos[val][2]]=1
		elif z==[0,1,2]:
			x=l-bpos[val][0]
			y=bpos[val][2]-r
			w.append((apos[val][0],apos[val][2],x,y))
		elif z==[0,2,2]:
			x=l-bpos[val][0]
			y=bpos[val][2]-r
			l2r.append((x,y))
		elif z==[1,1,1]:
			t[apos[val][0]]=1
			t[apos[val][1]]=1
			t[apos[val][2]]=1
		elif z==[1,1,2]:
			t[apos[val][0]]=1
			t[apos[val][2]]=1
		elif z==[1,2,2]:
			t[apos[val][0]]=1
		elif z==[2,2,2]:
			return False
		else:
			assert False
		
	if not issubseq():
		return False
	
	def conflict(xa,xb,ya,yb):
		return ya<=xa and xb<=yb
	
	for xa,xb in l2r:
		for ya,yb in r2l:
			if conflict(xa,xb,ya,yb):
				return False
	
	s=len(w)
	ts=twosat(s)
	
	for i in range(s):
		pa,pb,qa,qb=w[i]
		
		#left is ok?
		ok=True
		t[pa]=1
		if not issubseq():
			ok=False
		t[pa]=0;
		if ok:
			for xa,xb in l2r:
				if conflict(xa,xb,qa,qb):
					ok=False
		if not ok:
			ts.add(i*2+1,i*2+1)
		
		#right is ok?
		ok=True
		t[pb]=1;
		if not issubseq():
			ok=False
		t[pb]=0;
		if ok:
			for ya,yb in r2l:
				if conflict(qa,qb,ya,yb):
					ok=False
		if not ok:
			ts.add(i*2,i*2)
	
	for i in range(s):
		for j in range(i+1,s):
			p0a,p0b,q0a,q0b=w[i]
			p1a,p1b,q1a,q1b=w[j]
			t0=bpos[a[p0a]][1]
			t1=bpos[a[p1a]][1]
			
			#left-left is ok?
			ok=True
			if (p0a<p1a)!=(t0<t1):
				ok=False
			if not ok:
				ts.add(i*2+1,j*2+1)
				
			#left-right is ok?
			ok=True
			if (p0a<p1b)!=(t0<t1):
				ok=False
			if conflict(q1a,q1b,q0a,q0b):
				ok=False
			if not ok:
				ts.add(i*2+1,j*2)
			
			#right-left is ok?
			ok=True
			if (p0b<p1a)!=(t0<t1):
				ok=False;
			if conflict(q0a,q0b,q1a,q1b):
				ok=False
			if not ok:
				ts.add(i*2,j*2+1)
		
			#right-right is ok?
			ok=True
			if (p0b<p1b)!=(t0<t1):
				ok=False
			if not ok:
				ts.add(i*2,j*2);
		
	return ts.solve();


ans=10**18
for i in range(N):
	for j in range(i,N+1):
		if feasible(i,j):
			ans=min(ans,N-(j-i))

if ans==10**18:
	ans=-1

print(ans)
