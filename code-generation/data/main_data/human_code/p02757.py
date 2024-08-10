
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N,P=MI()
    S=input()
    
    if P==2 or P==5:
        ans=0
        for i in range(N):
            if int(S[i])%P==0:
                ans+=i+1
                
        print(ans)
        exit()
    
    
    
    from collections import defaultdict
    dd = defaultdict(int)
    
    now=0
    dd[0]=1
    for i in range(N):
        now=now+(pow(10,i,P)*int(S[-1-i]))
        now%=P
        dd[now]+=1
        
    ans=0
    for k,v in dd.items():
        ans+=(v*(v-1))//2
        
    print(ans)
    

main()
