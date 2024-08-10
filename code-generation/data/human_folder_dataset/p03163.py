# メイン関数
def main():
    # 入力データ
    N, W = map(int, input().split())
    w = []
    v = []
    for i in range(N):
        wi, vi = map(int, input().split())
        w.append(wi)
        v.append(vi)

    # dpテーブルの作成
    dp = [[0] * (W+1) for i in range(N)]
    for i in range(N):
        for j in range(W + 1):
            if j - w[i] >= 0:
                dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # 解答の出力
    print(dp[-1][-1])
    return

# 実行
if __name__ == '__main__':
    main()
