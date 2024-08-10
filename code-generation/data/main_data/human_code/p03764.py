import sys
sys.setrecursionlimit(10**8)

def sort(a):
	a.sort()

def rev(a):
	a.reverse()

def sd():
	return int(input())

def _sd():
	return map(int,input().split())

def sa():
	return list(map(int,input().split()))

def ss():
	return input()

def sf():
	return float(input())
 
def main():
	n,m=_sd()
	X=sa()
	Y=sa()
	sum_x=int(0)
	sum_y=int(0)
	mod=int((1e+9)+7)
	for i in range(1,n+1):
		sum_x+=(i+i-n-1)*X[i-1]
		sum_x%=mod
	for i in range(1,m+1):
		sum_y+=(i+i-m-1)*Y[i-1]
		sum_y%=mod
	print((sum_x*sum_y)%mod)
main()