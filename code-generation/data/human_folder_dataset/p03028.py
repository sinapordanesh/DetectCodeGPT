import sys

p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline()[:-1]
def pbit(aa,L):
    for a in aa:print(format(a,"b").zfill(L))
    print()

def main():
    n=II()
    aa=[[int(c) for c in SI()] for _ in range(n-1)]
    #p2D(aa)

    # 人iが勝てる相手をbitで管理する
    win=[0]*n
    for i,row in enumerate(aa,1):
        for j,a in enumerate(row):
            if a:win[i]|=1<<j
            else:win[j]|=1<<i
    #pbit(win,n)

    # dpl[i]...[j,i]の範囲で優勝できるjをbitで
    # dpr[i]...[i,j]の範囲で優勝できるjをbitで
    dpl=[1<<i for i in range(n)]
    dpr=[1<<i for i in range(n)]
    for d in range(1,n):
        for i in range(n-d):
            j=i+d
            if dpl[j] & dpr[i+1] & win[i]:dpl[j]|=1<<i
        for i in range(d,n):
            j=i-d
            if dpl[i-1] & dpr[j] & win[i]:dpr[j]|=1<<i
    #pbit(dpl,n)
    #pbit(dpr,n)
    #print(format(dpl[n-1]&dpr[0],"b").zfill(n))
    print(bin(dpl[n-1]&dpr[0]).count("1"))

main()