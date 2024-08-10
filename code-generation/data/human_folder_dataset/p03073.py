import math


def main():
    # n = int(input())
    # a, b = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    s = list(input())
    # 1010...
    count1 = 0
    # 0101...
    count2 = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != "1":
            count1 += 1
        if i % 2 != 0 and s[i] != "0":
            count1 += 1
        if i % 2 == 0 and s[i] == "1":
            count2 += 1
        if i % 2 != 0 and s[i] == "0":
            count2 += 1

    print(min(count1, count2))


if __name__ == '__main__':
    main()
