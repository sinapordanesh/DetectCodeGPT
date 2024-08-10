import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import bisect
    mod=10**9+7
    N,K=MI()
    A=LI()
    pos=[]
    zero=[]
    nega=[]
    for i in range(N):
        if A[i]>0:
            pos.append(A[i])
        elif A[i]==0:
            zero.append(A[i])
        else:
            nega.append(A[i]*-1)
            
    np=len(pos)
    nz=len(zero)
    nn=len(nega)
    
    pos.sort()
    zero.sort()
    nega.sort()
    
    inf=10**18 + 1
    
    #全部正で考える
    
    if K<=np * nn:
        # 答えが負になるパターン
        # 正の数で考えるので大きい方からK番目を考える
        # 二分探索*2
        # X以上になるものが，初めてK個以上になったタイミングが答え
        
        def ch(x):
            cnt=0
            for p in pos:
                t=(x+p-1)//p
                num=bisect.bisect_left(nega,t)
                cnt+=nn-num
            return cnt>=K
                
        
        ok=0
        ng=inf
        while ng-ok>1:
            x=(ok+ng)//2
            if ch(x):
                ok=x
            else:
                ng=x
        
        print(ok*-1)
        
    elif K<= np*nn + nz*(N-nz) + (nz*(nz-1))//2:
        print(0)
        
    else:
        # 答えが正になるパターン
        # 大きい方からK2= (N*(N-1))//2 - K番目を考える
        # 二分探索*2
        # X以上になるものが，初めてK2個以上になったタイミングが答え
        K2=(N*(N-1))//2 - K + 1
        # print(K2)
        
        def ch(x):
            cnt=0
            for p in pos:
                t=(x+p-1)//p
                num=bisect.bisect_left(pos,t)
                rem=np-num
                if t<=p:
                    rem-=1
                cnt+=rem
                
            for ne in nega:
                t=(x+ne-1)//ne
                num=bisect.bisect_left(nega,t)
                rem=nn-num
                if t<=ne:
                    rem-=1
                cnt+=rem
                
            cnt=cnt//2
            # print(x,cnt)
            return cnt>=K2
                
        
        ok=0
        ng=inf
        while ng-ok>1:
            x=(ok+ng)//2
            if ch(x):
                ok=x
            else:
                ng=x
        
        print(ok)
        
        
        

main()
