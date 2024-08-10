def main():
    N = int(input())
    n = 1
    # 1～n番目の問題を全部解いた時の点数が初めてN点以上になるnを求める
    while n * (n + 1) // 2 < N:
        n += 1
    # 後は間を抜いて、ジャストN点になるよう調整していく
    d = n * (n + 1) // 2 - N
    solve = [1] * (n + 1)  # 1-indexで扱うので0番目は使わない
    for i in range(n, 0, -1):
        if i <= d:
            d -= i
            solve[i] = 0
        if d == 0:
            break
    for i in range(1, n + 1):
        if solve[i] == 1:
            print(i)


if __name__ == '__main__':
    main()
