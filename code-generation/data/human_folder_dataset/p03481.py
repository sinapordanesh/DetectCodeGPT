#-*-coding:utf-8-*-
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    x,y=map(int,readline().split())
    ans=0
    while x<=y:
        x*=2
        ans+=1
    print(ans)

if __name__=="__main__":
    main()