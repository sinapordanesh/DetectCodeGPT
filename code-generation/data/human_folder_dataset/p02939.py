# coding: utf-8


def main():
    S = input()
    ans = 0
    a, b = '', ''

    for s in S:
        a += s
        if a != b:
            ans += 1
            b = a
            a = ''

    print(ans)

if __name__ == "__main__":
    main()
