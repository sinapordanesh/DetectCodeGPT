#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n = int(input())
    mod = 10**9+7
    power=1

    for i in range(1,n+1):
        power*=i
        power%=mod
    print(power)

if __name__=="__main__":
    main()