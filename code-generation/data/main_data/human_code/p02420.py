def main():
    while True:
        card = input()
        if card == '-':
            break
        shuffle = int(input())
        for _ in range(shuffle):
            index = int(input())
            card = card[index:] + card[:index]
        print(card)


if __name__ == '__main__':
    main()

