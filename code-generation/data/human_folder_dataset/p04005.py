# coding: utf-8

def main():
    N = sorted(list(map(int, input().split())))
    ans = N[0] * N[1] * (N[2] % 2)
    print(ans)

if __name__ == "__main__":
    main()
