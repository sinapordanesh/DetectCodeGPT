
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S="00"+input()
    S=S[::-1]
    N=len(S)-1
    
    def calc(x,nxt):
        # 今見てる数字,次の桁の数字,を受けて
        # 今使う,繰り上がり，を返す

        if x<=4:
            return x,0
        elif x>=6:
            return 10-x,1
        else:
            # 次が5なら，そのあと5以上ががくればお得，そうでなくとも損しない
            if nxt<5:
                return 5,0
            else:
                return 5,1
    
    kuri=0
    ans=0
    for i in range(N):
        now=int(S[i])
        nxt=int(S[i+1])
        now+=kuri
        temp,kuri = calc(now,nxt)
        
        ans+=temp
        
    print(ans)
        

main()
