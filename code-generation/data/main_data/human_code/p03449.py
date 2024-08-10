#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    maps=[]
    n = int(input())
    maps=[list(map(int,input().split())) for _ in range(2)]
    dp=[]
    for i in range(n):
        total=sum(maps[0][:i+1])+sum(maps[1][i:])
        dp.append(total)
    print(max(dp))

if __name__=="__main__":
    main()