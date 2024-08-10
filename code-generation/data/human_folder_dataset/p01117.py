def main():
    import sys
    from itertools import chain
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == m == 0:
            break

        A = list(chain.from_iterable(map(int, sys.stdin.readline().split()) for _ in range(m)))
        ans = 0
        for i in range(n):
            sm = sum(A[i::n])
            if ans < sm:
                ans = sm
        print(ans)

if __name__ == '__main__':
    main()
