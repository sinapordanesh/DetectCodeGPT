def main():
    n = int(input())
    taro, hanako = 0, 0
    for _ in range(n):
        cards = input().split()
        if cards[0] == cards[1]:
            taro += 1
            hanako += 1
        elif cards[0] != sorted(cards)[0]:
            taro += 3
        else:
            hanako += 3
    print(taro, hanako)


if __name__ == '__main__':
    main()

