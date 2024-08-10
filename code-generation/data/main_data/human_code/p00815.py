import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def solve():
    record = list(map(int,input().split()))
    while record[-1] != 0:
        record += list(map(int,input().split()))
    number_of_room = sum(1 if r > 0 else 0 for r in record) + 1
    G = [[] for _ in range(number_of_room)]
    deg = [0] * number_of_room
    parents = [-1] * number_of_room
    dist = [1000] * number_of_room
    dist[1] = 0

    now = 1
    cnt = 0
    for r in record[:-1]:
        if r > 0:
            cnt += 1
            if cnt > 1:
                G[cnt].append(now)
                G[now].append(cnt)
                deg[now] -= 1
                dist[cnt] = dist[now] + 1
                parents[cnt] = now
                deg[cnt] = r - 1
            else:
                deg[cnt] = r
            now = cnt
            while deg[now] <= 0 and now >= 0:
                now = parents[now]
        else:
            i = parents[now]
            while True:
                if dist[i] - dist[now] == r:
                    G[now].append(i)
                    G[i].append(now)
                    deg[i] -= 1
                    deg[now] -= 1
                    while deg[now] <= 0 and now >= 0:
                        now = parents[now]
                    break
                i = parents[i]
    
    for i in range(1,number_of_room):
        G[i].sort()
        print(i,*G[i])      

def main():
    N = int(input())
    for _ in range(N):
        solve()
    
if __name__ == '__main__':
    main()
