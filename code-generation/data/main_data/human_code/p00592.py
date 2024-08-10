# AOJ 1006: Boring Commercials
# Python3 2018.7.5 bal4u

import sys
from sys import stdin
input = stdin.readline

def d2t(d):	return (d//100)*60 + (d%100)

while True:
	n, p, q = map(int, input().split())
	if n == 0: break
	tbl = [0]*1500
	p, q = d2t(p), d2t(q)
	for i in range(n):
		k = 2*int(input())
		a = list(map(int, input().split()))
		for j in range(0, k, 2):
			t1, t2 = d2t(a[j]), d2t(a[j+1])
			for t in range(t1, t2): tbl[t] += 1
	ans = k = 0
	for t in range(p, q):
		if tbl[t] < n: k += 1
		elif k > 0: 
			if k > ans: ans = k
			k = 0
	if k > ans: ans = k
	print(ans)

