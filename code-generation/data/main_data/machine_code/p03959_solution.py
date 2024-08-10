def mountain_heights(N, Takahashi, Aoki):
    MOD = 10**9 + 7
    
    dp1 = [1] * N
    dp2 = [1] * N
    
    for i in range(1, N):
        if Takahashi[i] > Takahashi[i-1]:
            dp1[i] = dp1[i-1]
        else:
            dp1[i] = Takahashi[i]
    
    for i in range(N-2, -1, -1):
        if Aoki[i] > Aoki[i+1]:
            dp2[i] = dp2[i+1]
        else:
            dp2[i] = Aoki[i]
    
    answer = 1
    for i in range(N):
        h = min(dp1[i], dp2[i])
        if h < Takahashi[i] or h < Aoki[i]:
            answer = 0
            break
        answer = (answer * h) % MOD
    
    return answer

# Sample Input 1
print(mountain_heights(5, [1, 3, 3, 3, 3], [3, 3, 2, 2, 2])) # 4

# Sample Input 2
print(mountain_heights(5, [1, 1, 1, 2, 2], [3, 2, 1, 1, 1])) # 0

# Sample Input 3
print(mountain_heights(10, [1, 3776, 3776, 8848, 8848, 8848, 8848, 8848, 8848, 8848], [8848, 8848, 8848, 8848, 8848, 8848, 8848, 8848, 3776, 5])) # 884111967

# Sample Input 4
print(mountain_heights(1, [17], [17])) # 1