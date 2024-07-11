import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))


"""
全体のxor=S
赤のxor=xとすれば
求値は x+(S^x)の最大値
きつい

上の桁から見て，
Sのi桁目が0の時，その桁が1のものを奇数ずつ割り振りたい．
Sのi桁目が1の時，どんな分け方しても関係ない

上の桁から埋めたいというのはxを最大化したいというのと似ている．
Sのi桁目が1のぶんは先に計算しておく,かつ，各A[i]のその桁を0にしておけば，xを最大化したいという問題に帰着するか

xorの最大化，難しい．基底ベクトルに分解して，上の桁から足していく？
"""
def main():
    mod=10**9+7
    
    N=I()
    A=LI()
    
    S=0
    for i in range(N):
        S=S^A[i]
    
    M=61
    delete=[0]*M#消す桁
    
    ans=0
    for i in range(M):
        if (S>>i) & 1:
            delete[i]=1
            ans+=1<<i
            for j in range(N):
                if (A[j]>>i)&1:
                    A[j]-=1<<i
    
    #基底ベクトルを入れていく                
    vec=[]
    
    #二進数の桁数
    def dig_b(x):
        cnt=0
        while x!=0:
            x=x//2
            cnt+=1
        return cnt
    
    for i in range(N):
        now=A[i]
        d=dig_b(now)
        
        if vec==[]:
            vec.append((now,d))
        else:
            for v in vec:#各基底ベクトルと比較
                if v[1]==d:#今見てる数字と，基底ベクトルの最上位の桁数が同じなら潰せる
                    now=now^v[0]
                    d=dig_b(now)
            if now!=0:#0以外なら基底になる
                vec.append((now,d))
                vec.sort(reverse=True) #基底は大きい順に走査したいので
                
    temp=0
    for v in vec:
        temp2=temp^v[0]
        temp=max(temp,temp2)
        
    ans+=temp*2
    print(ans)
                    
                
        
    
                    
    
                    

        


main()
