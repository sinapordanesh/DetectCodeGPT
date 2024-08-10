import queue
n,q=int(input()),queue.Queue()
s=[set() for i in range(n+1)]
for i in range(2*n-2):
	u,v=map(int,input().split())
	if v in s[u]:
		q.put((u,v))
	else:
		s[u].add(v)
		s[v].add(u)
f=[i for i in range(n+1)]
def find(x):
	if f[x]==x:
		return x
	else:
		f[x]=find(f[x])
		return f[x]
while not q.empty():
	u,v=map(find,q.get())
	if u==v:
		continue
	if len(s[u])<len(s[v]):
		u,v=v,u
	s[u].remove(v)
	s[v].remove(u)
	for x in s[v]:
		s[x].remove(v)
		if u in s[x]:
			q.put((u,x))
		else:
			s[u].add(x)
			s[x].add(u)
	s[v],f[v]=[],u
root=find(1)
for i in range(2,n+1):
	if find(i)!=root:
		print("NO")
		break
else:
	print("YES")