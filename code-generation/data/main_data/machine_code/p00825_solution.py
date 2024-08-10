def concert_hall_scheduling():
    while True:
        n = int(input())
        if n == 0:
            break
        
        data = []
        for _ in range(n):
            data.append(list(map(int, input().split())))

        max_days = max(data, key=lambda x: x[1])[1]
        dp = [0] * (max_days + 1)

        for i in range(1, max_days + 1):
            dp[i] = dp[i - 1]
            for j in data:
                if j[1] == i:
                    dp[i] = max(dp[i], dp[j[0] - 1] + j[2])

        print(dp[max_days])

concert_hall_scheduling()