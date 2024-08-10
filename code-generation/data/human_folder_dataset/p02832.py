#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main2():
    numbers=[]
    N = int(input())
    numbers=list(map(int,input().split()))
    n=1

#条件が1<=n<=200kのため1から順に数えてlist内を調査した場合の最大値+1をnに記入
    for x in numbers:
        if x ==n:
            n+=1

#条件から+1まで数えてしまうため、nを+1して調整
    answer = N - n +1

    if answer==N:
        answer=-1
    print(answer)

def main():
    numbers=[]
    n = int(input())
    numbers=list(map(int,input().split()))
    buffer=[0]
    for i in range(1,n+1):
        search_range=numbers[i-1:]
        out_range=len(numbers[:i-1])
        if i not in search_range and len(buffer)==1:
            print(-1)
            exit()
        elif i not in search_range or i==n:
            break
        else:
            index=search_range.index(i)
            buffer.append(index-sum(buffer))
    print(sum(buffer))

if __name__=="__main__":
    main2()