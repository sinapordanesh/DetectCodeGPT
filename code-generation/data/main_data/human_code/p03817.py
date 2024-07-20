import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    x = I()
    ans = x//11*2
    num = x%11
    if num==0:
        pass
    elif num<=6:
        ans += 1
    else:
        ans += 2

    print(ans)
main()
