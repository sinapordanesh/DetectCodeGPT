# AOJ 1058 Winter Bells
# Python3 2018.7.7 bal4u

import heapq
INF = 0x7fffffff

def dijkstra(V, to, start):
	dist, path = [INF]*V, [0]*V
	Q = []
	dist[start], path[start] = 0, 1
	heapq.heappush(Q, (0, start))
	while Q:
		t, s = heapq.heappop(Q)
		if dist[s] < t: continue
		for e, cost in to[s]:
			nt = t + cost
			if dist[e] < nt: continue
			if dist[e] > nt:
				path[e] = 0
				dist[e] = nt
				heapq.heappush(Q, (nt, e))
			path[e] += path[s]
	return [dist, path]
	
while True:
	n, m, p = map(int, input().split())
	if n == 0: break
	to = [[] for i in range(n)]
	for i in range(m):
		a, b, c = map(int, input().split())
		to[a].append((b, c))
		to[b].append((a, c))
	dist1, path1 = dijkstra(n, to, 0)
	dist2, path2 = dijkstra(n, to, n-1)
	for i in range(p):
		c = int(input())
		if dist1[c]+dist2[c] == dist2[0]:
			print((path1[c]*path2[c])/path2[0])
		else: print(0)
	print()
