#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    k, *a = map(int, input().split())
    ans = set(a)
    for i in range(n - 1):
        k, *a = map(int, input().split())
        ans = ans & set(a)
    print(len(ans))


if __name__ == "__main__":
    main()
