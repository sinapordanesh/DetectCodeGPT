def main():
    n = int(input())
    p_lst = list(map(int, input().split()))
    count = 0

    tmp = 0
    for i in range(n):
        p = p_lst[i]

        if p == (i + 1):
            if tmp == 1:
                tmp = 0
            else:
                count += 1
                tmp += 1
        else:
            tmp = 0

    print(count)


if __name__ == '__main__':
    main()