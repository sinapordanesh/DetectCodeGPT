def solve(a, b):
    if a * b % 2 == 0:
        print('Even')
    else:
        print('Odd')


if __name__ == '__main__':
    a, b = map(int, input().split())
    solve(a, b)
