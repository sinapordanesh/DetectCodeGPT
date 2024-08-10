import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()

    ans = 1
    while N >= 3:
        N -= 3
        ans += 1
    
    ans -= 1
    print(ans)






if __name__ == "__main__":
    main()