def main():
    N, K = map(int, input().split())
    ans = 0
    for b in range(1, N+1):
        p = N//b
        r = N%b
        ans += p * max(0, b-K) + max(0, r+1-K) - (K==0)
    print(ans)

if __name__ == "__main__":
    main()
