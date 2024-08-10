import sys


def main():
    n = int(sys.stdin.readline())
    i = 1
    while i <= n:
        x = i
        if x % 3 == 0:
            print(' {}'.format(i), end='')
        else:
            while x > 1:
                if int(x) % 10 == 3:
                    print(' {}'.format(i), end='')
                    break
                x /= 10
        i += 1
    print()
    return


if __name__ == '__main__':
    main()

