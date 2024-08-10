# coding: utf-8

def main():
    N = sorted(list(map(int, input().split())))
    ans = N[2] - N[1]
    d = N[1] - N[0]
    if d % 2 != 0:
        ans += 2
    ans += d // 2
    print(ans)

if __name__ == "__main__":
    main()
