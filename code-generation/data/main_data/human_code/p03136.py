import sys
input = sys.stdin.readline


def main():
    N = int(input())
    L = list(map(int, input().split()))

    if max(L) < sum(L) - max(L):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

