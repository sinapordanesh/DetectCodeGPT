# coding: utf-8


def main():
    N = int(input())
    ans = 'Yes'
    t, x, y = 0, 0, 0
    for _ in range(N):
        nt, nx, ny = map(int, input().split())
        d = abs(x - nx) + abs(y - ny)
        if d > nt - t or (nt - t - d) % 2 != 0:
            ans = 'No'
            break
        t, x, y = nt, nx, ny

    print(ans)

if __name__ == "__main__":
    main()
