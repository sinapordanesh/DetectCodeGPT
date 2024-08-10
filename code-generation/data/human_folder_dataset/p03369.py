from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    S = list(input())

    c = 0
    for s in S:
        c += s == "o"
    
    print(700+100*c)




if __name__ == "__main__":
    main()