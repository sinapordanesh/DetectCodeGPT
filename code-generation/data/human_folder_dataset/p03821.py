#!/usr/bin/env python3

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        tmp = ans + ab[n - i - 1][0]
        cnt = tmp % ab[n - i - 1][1]
        if cnt:
            ans += ab[n - i - 1][1] - cnt

    print(ans)


if __name__ == "__main__":
    main()
