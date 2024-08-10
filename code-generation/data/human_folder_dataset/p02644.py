from heapq import heappop, heappush 
from collections import deque
def dijkstra(xs, ys, xg, yg,h,w,k,field):
    # que->(cost, x, y, direction)
    inf = 1e18
    dist = [[inf]*w for _ in range(h)]
    dist[xs][ys] = 0
    que = deque([(0, xs, ys)])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while que:
        cost, x, y = que.popleft()
        if cost > dist[x][y]:
            continue
        for v in range(4):
            nx, ny = x, y
            for _ in range(k):
                nx += dx[v]
                ny += dy[v]
                if not field[nx][ny]:
                    break
                if dist[nx][ny]<=dist[x][y]:
                    break
                if dist[nx][ny] > dist[x][y]+1:
                    dist[nx][ny] = dist[x][y]+1
                    que.append((dist[nx][ny], nx, ny))

    if dist[xg][yg] == inf:
        print(-1)
    else:
        print(dist[xg][yg])

        

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    h, w, k = map(int, input().split())
    xs, ys, xg, yg = map(int, input().split())
    field = [[False]*(w+2) for _ in range(h+2)]
    for i in range(h):
        # False で覆うことでx,yの制限をなくす。
        s = [True if _ == '.' else False for _ in input()]
        field[i+1] = [False]+s+[False]
    h += 2
    w += 2
    dijkstra(xs, ys, xg, yg, h, w, k, field)

if __name__ == '__main__':
    main()
