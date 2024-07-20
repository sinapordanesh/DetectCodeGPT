import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    A = input_int_list()
    for i in range(n):
        A[i] = A[i] - (i + 1)

    A.sort()

    if n % 2 == 0:
        mid = (A[(n - 1) // 2] + A[((n - 1) // 2) + 1]) // 2
    else:
        mid = A[(n - 1) // 2]

    tmp0 = 0
    tmp1 = 0

    for a in A:
        tmp0 += abs(a - mid)
        tmp1 += abs(a - mid - 1)

    print(min(tmp0, tmp1))

    return


if __name__ == "__main__":
    main()
