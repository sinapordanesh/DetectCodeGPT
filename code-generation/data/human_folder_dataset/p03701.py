def resolve():
    import sys
    input = sys.stdin.readline
    # 整数 1 つ
    n = int(input())
    # 整数複数個
    # a, b = map(int, input().split())
    # 整数 N 個 (改行区切り)
    S = [int(input()) for i in range(n)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    Score = [[0] * 10001 for _ in range(n+1)]

    for i in range(n):
        for j in range(10001):
            if j+S[i]<=10000:
                Score[i+1][j+S[i]] = max(Score[i+1][j+S[i]], Score[i][j] + S[i])
            Score[i+1][j] = max(Score[i+1][j], Score[i][j])

    ansmax = 0
    for i in range(n+1):
        for j in range(10001):
            if Score[i][j] % 10 != 0:
                ansmax = max(ansmax, Score[i][j])

    print(ansmax)


resolve()