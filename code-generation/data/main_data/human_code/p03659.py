# C - Splitting Pile
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    cnt = 0
    ans = float('inf')

    for i in range(n-1):
        cnt += a[i]
        ans = min(ans, abs(a_sum-cnt*2))
    else:
        print(ans)


if __name__ ==  "__main__":
    main()