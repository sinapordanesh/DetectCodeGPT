
def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 1 << 60

    for i in range(N - K + 1):
        l = A[i]
        r = A[i + K - 1]
        l_to_r = abs(l) + abs(l - r)
        r_to_l = abs(r) + abs(r - l)
        res = min(l_to_r, r_to_l)
        ans = min(ans, res)

    print(ans)


if __name__ == "__main__":
    resolve()
