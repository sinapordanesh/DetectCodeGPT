def iroha():
    a, b = map(int, input().split())

    num = a + b
    if num >= 24:
        new_num = num % 24
        print(new_num)
    else:
        print(num)

if __name__ == "__main__":
    iroha()

