#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    d,n = map(int,input().split())

    if n==100:
        print((100**d)*101)
        exit()
    else:
        print((100**d)*n)

if __name__=="__main__":
    main()