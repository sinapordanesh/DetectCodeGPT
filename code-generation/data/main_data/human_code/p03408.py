import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return float(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

from collections import defaultdict

def main():
	s=defaultdict(int)
	n=II()
	for _ in range(n):
		s[RD()]+=1
	m=II()
	for _ in range(m):
		s[RD()]-=1

	ans=0
	for k,v in s.items():
		ans=max(ans,v)
	print(ans)





if __name__ == "__main__":
	main()
