def main(n,x):
    ret=1
    mod=10**9+7
    stc=[]
    for y in x:
        if 2*(len(stc)+1)-1<=y:
            stc.append(y)
        else:
            ret*=len(stc)+1
            ret%=mod
    for i in range(len(stc)):
        ret*=i+1
        ret%=mod
    return ret

n=int(input())
#a=list(input())
#a=list(map(int,input().split()))
#b=list(map(int,input().split()))
#ab=[list(map(int,input().split())) for _ in range(n)]
#n,k,q=map(int,input().split())
x=list(map(int,input().split()))
print(main(n,x))
