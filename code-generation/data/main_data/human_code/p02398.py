import sys


def main():
    a, b, c = [int(i) for i in sys.stdin.readline().split(' ')]
    divisors = 0
    for i in range(a, b+1):
        if i == 0:
            continue
        elif c % i == 0:
            divisors += 1
    print(divisors)
    return


if __name__ == '__main__':
    main()

