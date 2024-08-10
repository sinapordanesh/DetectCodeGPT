def taros_shopping():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        prices = list(map(int, input().split()))
        max_sum = 0
        for i in range(n):
            for j in range(i + 1, n):
                if prices[i] + prices[j] <= m:
                    max_sum = max(max_sum, prices[i] + prices[j])
        if max_sum == 0:
            print("NONE")
        else:
            print(max_sum)

taros_shopping()