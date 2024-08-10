import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""
とりあえず，数字ではなく，数字の出現回数C[i]を持つ．

Kが変化すると色々と変わるので，Kごとに見ようとすると割と大変そう，1つのkごとにO(N)すらかけられない，というか計算大変そう．
(カードがT種類あるとして，k>Tは全部0だったりする．Kの区間に対して一気に答えを出す方法はありそう．)

食べる回数をmとして，mごとに最大のKを求める．

m回食べるということは，各数字につき最大m回までしか食べられないということ
食べられる枚数の総数はΣ(min(m,C[i]))．このときの最大のKは，総数//m

C[i]を昇順に並べておけば二分探索で
min(m,C[i])=C[i]の範囲がわかり，累積和をとっておればこの区間の合計がO(1)で求まる
"""
def main():
    import bisect
    
    N=I()
    A=LI()
    from collections import defaultdict
    dd = defaultdict(int)
    
    for i in range(N):
        dd[A[i]]+=1
        
    L=[]
    for k,v in dd.items():
        L.append(v)
        
    L.sort()
    nl=len(L)
    S=[0]*(nl+1)
    for i in range(nl):
        S[i+1]=S[i]+L[i]
        
    ans=[0]*(N+1)
    
    for m in range(1,N+1):
        temp=0
        num=bisect.bisect_left(L,m)
        temp+=S[num]
        temp+=(nl-num)*m
        
        maxk=temp//m
        ans[maxk]=max(ans[maxk],m)
        # print(m,temp,maxk)
        
    # print(ans)
        
    M=0
    for i in range(N,-1,-1):
        M=max(M,ans[i])
        ans[i]=M
        
    for i in range(1,N+1):
        print(ans[i])
        
        
        
    
    

main()
