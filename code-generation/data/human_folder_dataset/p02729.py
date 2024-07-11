def main():
    n, m = map(int, input().split())
    # nは偶数、mは奇数
    # n+mから2つ選ぶ選び方は
    # n:m = 0:2 和は 偶数、選び方はmC2
    # n:m = 1:1 和は 奇数 （今回はこれは含めない）
    # n:m = 2:0 和は 偶数、選び方はnC2
    cnt = 0
    if m >= 2:
        cnt += m * (m -1) // 2
    if n >=2:
        cnt += n * (n -1) // 2
    print(cnt)

if __name__ == '__main__':
    main()