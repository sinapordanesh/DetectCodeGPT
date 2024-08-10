import sys
input = sys.stdin.readline

import collections
import random

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def dist(x1,y1,x2,y2):
	return abs(x1-x2)+abs(y1-y2)

def main():
	N = int(input())
	vS = [input().rstrip() for _ in [0,]*N]
	oA = ord("a")
	vD = [chr(i+oA) for i in range(26)]
	#vD += [".","#"]

	#res = 0
	vR = [1001001001,]*26
	for s in vS:
		for i,d in enumerate(vD):
			vR[i] = min(vR[i], s.count(d))
	
	res = ""
	for r,d in zip(vR,vD):
		res += d*r
	print(res)
	#sT = "No Yes".split()
	#print(sT[res])
	

if __name__ == "__main__":
	main()
