# coding: utf-8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    e = 0
    for a in A:
        if a % 2 == 0:
            e += 1

    ans = 3 ** N - 2 ** e

    print(ans)

if __name__ == "__main__":
    main()
