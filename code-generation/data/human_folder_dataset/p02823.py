# coding: utf-8


def main():
    N, A, B = map(int, input().split())

    ans = (B - A) // 2 if (B - A) % 2 == 0 else min(A - 1, N - B) + 1 + (B - A - 1) // 2

    print(ans)

if __name__ == "__main__":
    main()
