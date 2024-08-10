def ok(N, A):
    return all([a <= N - 1 for a in A])


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while not ok(N, A):
        n = 0
        # 「全てに1を足して、特定のものからN+1を引く」で等価な操作になる
        for i in range(N):
            c = A[i] // N
            n += c
            A[i] -= c * (N + 1)
        for i in range(N):
            A[i] += n
        ans += n
    print(ans)


if __name__ == '__main__':
    main()
