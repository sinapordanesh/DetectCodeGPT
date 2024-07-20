def main():
    w = input()
    wards = []
    while True:
        wards.extend(ward for ward in input().split())
        if wards[-1] == 'END_OF_TEXT':
            break
    num = 0
    for ward in map(lambda ward: ward.lower(), wards):
        if ward == w:
            num += 1
    print(num)


if __name__ == '__main__':
    main()

