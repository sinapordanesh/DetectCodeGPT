import sys
sys.setrecursionlimit(10**6)
n = int(input())
p = list(map(int, input().split()))
c = [[] for _ in range(n)]
is_leaf = [True for _ in range(n)]
for i in range(n):
	p[i] -= 1
	c[p[i]].append(i)
	is_leaf[p[i]] = False

if sum(is_leaf) == 0:
	if n%2 == 0:
		print("POSSIBLE")
	else:
		print("IMPOSSIBLE")
	sys.exit()

for i in range(n):
	if is_leaf[i]:
		cur = i
		break

visited_set = {cur}
visited_list = [cur]
while p[cur] not in visited_set:
	visited_list.append(p[cur])
	visited_set.add(p[cur])
	cur = p[cur]

root = p[cur]

grundy = [-1 for _ in range(n)]
g_set = [set() for _ in range(n)]

def dfs(x):
	res = 0
	for v in c[x]:
		dfs(v)
		g_set[x].add(grundy[v])
	while res in g_set[x]:
		res += 1
	grundy[x] = res
	return res

loop = [False for _ in range(n)]
loop[root] = True
ind = len(visited_list)-1
while visited_list[ind] != root:
	loop[visited_list[ind]] = True
	ind -= 1
#print(loop)

for i in range(n):
	if loop[i]:
		for x in c[i]:
			if not loop[x]:
				dfs(x)
				g_set[i].add(grundy[x])

cand = []
num = 0
while num in g_set[root]:
	num += 1
cand.append(num)
num += 1
while num in g_set[root]:
	num += 1
cand.append(num)

for x in cand:
	cur = root
	grundy[root] = x
	while True:
		num = 0
		while num in g_set[p[cur]] or num == grundy[cur]:
			num += 1
		grundy[p[cur]] = num
		if p[cur] == root:
			break
		cur = p[cur]
	if grundy[root] == x:
		#print(grundy)
		print("POSSIBLE")
		sys.exit()

print("IMPOSSIBLE")