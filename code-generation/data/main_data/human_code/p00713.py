import math


def find_point(x1, y1, x2, y2):
    # 二頂点(x1,y1),(x2,y2)を円周上にもつ時の半径1の円の中心
    if (x1-x2)**2+(y1-y2)**2 > 4:
        return False
    mx, my = (x1+x2)/2, (y1+y2)/2
    L = math.sqrt((y2-y1)**2+(x2-x1)**2)
    k = math.sqrt(1-((y2-y1)**2+(x2-x1)**2)/4)
    # (mx,my)+-(k/L)(-y2+y1,x2-x1)
    X1, Y1 = mx+(k/L)*(-y2+y1), my+(k/L)*(x2-x1)
    X2, Y2 = mx-(k/L)*(-y2+y1), my-(k/L)*(x2-x1)
    return ((X1, Y1), (X2, Y2))


def solve():
    N = int(input())
    if N == 0:
        return
    que = [tuple(map(float, input().split())) for _ in range(N)]
    ans = 1
    for i in range(N):
        for j in range(i+1, N):
            A = find_point(que[i][0], que[i][1], que[j][0], que[j][1])
            if A != False:
                a, b = A
                suba = 0
                subb = 0
                for k in range(N):
                    if math.hypot(que[k][0]-a[0], que[k][1]-a[1]) < 1+10**(-7):
                        suba += 1
                    if math.hypot(que[k][0]-b[0], que[k][1]-b[1]) < 1+10**(-7):
                        subb += 1
                ans = max(ans, suba, subb)
    print(ans)
    return solve()


def main():
    solve()


if __name__ == "__main__":
    main()
