def replace_digits(n):
    n = str(n)
    new_num = ''
    for digit in n:
        if digit == '1':
            new_num += '9'
        else:
            new_num += '1'
    return int(new_num)