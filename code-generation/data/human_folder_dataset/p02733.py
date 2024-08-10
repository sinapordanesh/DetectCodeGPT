def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H,W,K=MI()
    S=[]
    for _ in range(H):
        s=input()
        S.append(s)
        
    # Hに関してbit全探索
    import itertools
    
    inf=10**10
    ans=inf
    
    import bisect
    for ite in itertools.product([0,1], repeat=H-1):
        temp=sum(ite)
        g=[-1]#グループに分ける，区切り(末尾)の数字をいれる
        for i in range(len(ite)):
            if ite[i]==1:
                g.append(i)
        
        M=len(g)
        cnt=[0]*M#グループ毎
        
        flag=1#無理かどうか
        for j in range(W):
            if flag==0:
                break
            cnt2=[0]*M#各列用
            
            #数える
            for i in range(H):
                if S[i][j]=="1":
                    num=bisect.bisect_left(g,i)-1
                    cnt[num]+=1
                    cnt2[num]+=1
            
            #無理
            for i in range(M):
                if cnt2[i]>K:
                    temp=inf
                    flag=0
                    break
                
            #わるか確認
            flag2=0
            for i in range(M):
                if cnt[i]>K:
                    flag2=1
                    break
            #わる
            if flag2:
                for i in range(M):
                    cnt[i]=cnt2[i]
                temp+=1
                
        # print(ite,temp,g)
                    
        ans=min(ans,temp)
        
    print(ans)
                  
                
                

main()
