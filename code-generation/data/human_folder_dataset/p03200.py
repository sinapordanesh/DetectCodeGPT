# coding: utf-8

def main():
    S = list(input())
    b = 0
    ans = 0
    for s in S:
        if s == 'B':
            b += 1
        else:
            ans += b

    print(ans)

if __name__ == "__main__":
    main()
