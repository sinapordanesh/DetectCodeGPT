import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,X=mi()
    L=list(mi())

    d = 0
    ans = 1
    for i in range(N):
        d = d + L[i]
        ans += d <= X

    print(ans)



if __name__ == "__main__":
    main()