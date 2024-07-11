import sys


def main():
    while True:
        list1 = [i for i in sys.stdin.readline().split()]
        if '?' in list1:
            break
        a, b, op = int(list1[0]), int(list1[2]), list1[1]
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        else:
            print(int(a / b))
    return


if __name__ == '__main__':
    main()

