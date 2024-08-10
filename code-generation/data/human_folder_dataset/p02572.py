def main(N, A):
    ans = 0
    culm = sum(A)
    for i in range(N-1):
        culm -= A[i]
        ans += A[i]*culm
        ans %= 10**9 + 7
    return ans

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = main(N, A)
    print(ans)

