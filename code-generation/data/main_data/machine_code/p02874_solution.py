def maximum_joyfulness(N, LR):
    LR.sort(key=lambda x: x[1])
    left_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        left_sum[i] = left_sum[i - 1] + LR[i - 1][0]
    
    right_sum = [0] * (N + 2)
    for i in range(N, 0, -1):
        right_sum[i] = right_sum[i + 1] + LR[i - 1][1]
    
    max_joy = 0
    for i in range(1, N + 1):
        max_joy = max(max_joy, left_sum[i] + right_sum[i + 1])
    
    return max_joy

# Sample Input
print(maximum_joyfulness(4, [[4, 7], [1, 4], [5, 8], [2, 5]]))
print(maximum_joyfulness(4, [[1, 20], [2, 19], [3, 18], [4, 17]]))
print(maximum_joyfulness(10, [[457835016, 996058008], [456475528, 529149798], [455108441, 512701454], [455817105, 523506955], [457368248, 814532746], [455073228, 459494089], [456651538, 774276744], [457667152, 974637457], [457293701, 800549465], [456580262, 636471526]]))