def sum_of_digits():
    while True:
        num = input()
        if num == '0':
            break
        total = sum(int(digit) for digit in num)
        print(total)

sum_of_digits()