def solve():
    N, M = [int(i) for i in input().split()]
    D = [[int(i) for i in input().split()] for _ in range(N)]
    D.sort(key=lambda x: x[0])
    ans = 0
    for d in D:
        a, b = d
        ans += a * min(M, b)
        M -= min(M, b)
        if M == 0:
            print(ans)
            exit()

if __name__ == "__main__":
    solve()