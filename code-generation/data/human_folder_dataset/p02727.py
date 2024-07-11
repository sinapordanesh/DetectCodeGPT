import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    x, y, a, b, c = input_int_list()
    P = [-1] + sorted(input_int_list())  # 番兵
    Q = [-1] + sorted(input_int_list())
    R = [-1] + sorted(input_int_list())
    A = []
    B = []
    C = []
    for i in range(x + y):
        if R[-1] >= P[-1] and R[-1] >= Q[-1]:
            C.append(R.pop())
        elif P[-1] >= Q[-1] and P[-1] >= R[-1]:
            A.append(P.pop())
        else:
            B.append(Q.pop())
    if len(A) <= x and len(B) <= y:
        print(sum(A) + sum(B) + sum(C))
    elif len(A) > x:
        for j in range(len(A) - x):
            if R[-1] >= Q[-1]:
                C.append(R.pop())
            else:
                B.append(Q.pop())
        print(sum(A[:x]) + sum(B) + sum(C))
    elif len(B) > y:
        for j in range(len(B) - y):
            if R[-1] >= P[-1]:
                C.append(R.pop())
            else:
                A.append(P.pop())
        print(sum(A) + sum(B[:y]) + sum(C))

    return


if __name__ == "__main__":
    main()
