def main():
    # n = int(input())
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    s = list(input())
    # h = [int(input()) for _ in rane(n)]
    count0 = 0
    count1 = 0
    for i in s:
        if i == "0":
            count0 += 1
        else:
            count1 += 1

    print(min(count0, count1)*2)


if __name__ == '__main__':
    main()
