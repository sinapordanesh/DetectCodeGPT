# tenka1-2018C - Align
def main():
    N, *A = map(int, open(0).read().split())
    A.sort()
    if N & 1:
        low, high, mid = A[: N // 2], A[N // 2 + 1 :], A[N // 2]
        x = (sum(high) - sum(low)) * 2 - mid + low[-1]
        y = (sum(high) - sum(low)) * 2 + mid - high[0]
        ans = max(x, y)
    else:
        low, high = A[: N // 2], A[N // 2 :]
        ans = (sum(high) - sum(low)) * 2 - high[0] + low[-1]
    print(ans)


if __name__ == "__main__":
    main()