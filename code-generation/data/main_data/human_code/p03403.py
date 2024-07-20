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


def main():
	n=II()
	A=[0]+LI()+[0]
	total=0


	for i,j in zip(A[1:],A[:-1]):
		total+=abs(i-j)


	for i in range(1,n+1):
		print(total-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))











if __name__ == "__main__":
	main()
