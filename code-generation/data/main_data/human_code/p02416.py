def main():

    while True:
        num = input()
        if num == '0':
            break
        else:
            count = 0
            for s in num:
                count += int(s)
            print(count)

if __name__ == '__main__':
    main()
