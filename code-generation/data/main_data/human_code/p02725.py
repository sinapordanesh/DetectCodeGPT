import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    K,N=MI()
    A=LI()
    S=sum(A)
    L=[]
    for i in range(N-1):
        temp=A[i+1]-A[i]
        L.append(temp)
        
    L.append(A[0]+K-A[-1])
    M=max(L)
    
    print(K-M)

main()
