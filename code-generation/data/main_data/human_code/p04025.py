def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = float('inf')
    for k in range(min(A), max(A)+1):
        cost = 0
        for a in A:
            cost += (a-k)**2
        ans = min(ans, cost)
        if ans == 0:
            break
    print(ans)

if __name__ == "__main__":
    main()
