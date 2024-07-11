import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    md=10**9+7
    n=II()
    aa=LI()
    cs=[0]
    for a in aa:cs.append(cs[-1]^a)
    #print(cs)

    cnt={}
    cnt0=[1]*len(cs)
    for i,s in enumerate(cs[1:],1):
        if s==0:
            cnt0[i]=cnt0[i-1]+1
        elif s in cnt:
            cnt0[i]=cnt0[i-1]
            c0=cnt0[i]-cnt0[cnt[s][2]]
            cnt[s][0]=(cnt[s][0]+cnt[s][1]*c0)%md
            cnt[s][1]=(cnt[s][1]+cnt[s][0])%md
            cnt[s][2]=i
        else:
            cnt0[i]=cnt0[i-1]
            cnt[s]=[1,1,i]
    #print(cnt)
    #print(cnt0)

    if cs[-1]==0:ans=sum(v[1] for v in cnt.values())+pow(2,cnt0[-1]-2,md)
    else:ans=cnt[cs[-1]][0]
    print(ans%md)

main()