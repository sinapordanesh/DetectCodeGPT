def solve():
    MOD = 1000000007

    N = int(input())
    balls = [list(map(int, input().split())) for _ in range(2*N)]

    balls.sort()
    cnt = 1
    ans = 1
    for i in range(1, 2*N):
        if balls[i][1] < balls[i-1][1]:
            ans = (ans * cnt) % MOD
            cnt -= 1
        else:
            cnt += 1

    print(ans)

solve()