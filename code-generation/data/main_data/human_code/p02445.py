# coding=utf-8


def partial_swap(origin, begin, end, begin2):
    for i in range(end-begin):
        origin[begin+i], origin[begin2+i] = origin[begin2+i], origin[begin+i]

    return origin


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    for i in range(Q):
        b, e, t = map(int, input().split())
        A = partial_swap(A, b, e, t)

    print(' '.join(map(str, A)))

