def main():
    N = int(input())
    A, B, C = [], [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(a+b)
    C.sort(reverse=True)
    ans = 0
    for i in range(N//2+N%2):
        ans += C[2*i]
    ans -= sum(B)
    print(ans)

if __name__ == "__main__":
    main()
