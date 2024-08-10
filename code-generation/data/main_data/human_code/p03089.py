mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    B = list(map(int, input().split()))

    ans = []
    for _ in range(N):
        j = -1
        for i in range(len(B)):
            if B[i] == i+1:
                j = i
        if j == -1:
            print(-1)
            exit()
        ans.append(j+1)
        B.pop(j)
    for a in ans[::-1]:
        print(a)


if __name__ == '__main__':
    main()
