import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,L=map(int,input().split())
    T=[int(input()) for _ in range(n)]
    s=0
    from math import pi
    from cmath import rect
    for j in range(n):
        for i in range(j): # 0<=i<j<=n-1
            s+=-rect(1,(T[i]+T[j])*pi/L)*(j-i-1) # Ti<T<Tj なるTの個数はj-i-1
            s+= rect(1,(T[i]+T[j])*pi/L)*(n-(j-i+1)) # T<Ti, Tj<T なるTの個数はn-(j-i+1)
    s/=n*(n-1)*(n-2)/6
    print(s.real,s.imag)
resolve()