def maximum_profit():
    N = int(input())
    beasts = []
    for _ in range(N):
        x, s = map(int, input().split())
        beasts.append((x, s))
    
    max_profit = 0
    for i in range(N):
        for j in range(i, N):
            L = beasts[i][0]
            R = beasts[j][0]
            profit = sum(beast[1] for beast in beasts if L <= beast[0] <= R) - (R - L)
            max_profit = max(max_profit, profit)
    
    print(max_profit)