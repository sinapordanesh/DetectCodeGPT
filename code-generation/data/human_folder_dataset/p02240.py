# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 10:14:13 2018
ALDS1_11_D
@author: maezawa
"""

n, m = list(map(int, input().split()))
v = [-1 for _ in range(n)]
stack = []
adj = [[] for _ in range(n)]
for i in range(m):
    s, t = list(map(int, input().split()))
    adj[s].append(t)
    adj[t].append(s)
#print(*adj, sep='\n')
def dfs(u, color):
    if v[u] > 0:
        return 0
    stack.append(u)
    while stack:
        current = stack[-1]
        v[current] = color
        #print(u, current, stack)
        flag = 0
        for k in adj[current]:
            if v[k] > 0:
                continue
            stack.append(k)
            flag = 1
        if flag == 0:
            stack.pop()
    return 1

color = 1
for start in range(n):
    if dfs(start, color) == 1:
        color += 1
#for i in range(n):        
#    print('color:{} for node:{}'.format(i, v[i]))

q = int(input())
for i in range(q):
    s, t = list(map(int, input().split()))
    if v[s] == v[t]:
        print('yes')
    else:
        print('no')
