def simple_calculator():
    while True:
        data = input().split()
        a, op, b = data
        if op == '?':
            break
        a = int(a)
        b = int(b)
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            print(a // b)

simple_calculator()