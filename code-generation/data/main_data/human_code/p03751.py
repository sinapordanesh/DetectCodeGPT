def main():
    N = int(input())
    S = [input() for _ in range(N)]
    t = input()
    mn = 1
    mx = N+1
    for s in S:
        smin = s.replace("?", "a")
        smax = s.replace("?", "z")
        if t < smin:
            mx -= 1
        if smax < t:
            mn += 1
    ans = list(range(mn, mx+1))
    print(*ans)


if __name__ == "__main__":
    main()
