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
    L1 = [None] + list(input()) + [None]
    L2 = [None] + list(input()) + [None]
    seq = []
    if L1[1] == L2[1]:  # 縦ドミノ
        L1[1] = L2[1] = "#"
        seq.append("X")
    elif L1[1] == L1[2]:  # 横ドミノ
        L1[1] = L1[2] = L2[1] = L2[2] = "#"
        seq.append("Y")

    for i in range(1, n + 1):
        if L1[i] == "#":
            continue
        else:
            if L1[i] == L2[i]:
                seq.append("X")
                L1[i] = "#"
            elif L1[i] == L1[i + 1]:
                seq.append("Y")
                L1[i] = L1[i + 1] = "#"
    if seq[0] == "X":
        ans = 3
    elif seq[0] == "Y":
        ans = 6

    for i in range(1, len(seq)):
        if seq[i - 1] == "X":
            if seq[i] == "X":
                ans *= 2
            elif seq[i] == "Y":
                ans *= 2
        elif seq[i - 1] == "Y":
            if seq[i] == "X":
                ans *= 1
            elif seq[i] == "Y":
                ans *= 3
        ans %= 1000000007
    print(ans)
    return


if __name__ == "__main__":
    main()
