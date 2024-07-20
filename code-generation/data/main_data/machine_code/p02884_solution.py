import numpy as np

def escape_cave(N, M, passages):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    
    for passage in passages:
        adj_list[passage[0]].append(passage[1])
    
    dp = np.zeros(N+1)
    dp[N] = 0
    
    for i in range(N-1, 0, -1):
        if len(adj_list[i]) == 0:
            dp[i] = dp[i+1]
        else:
            for j in adj_list[i]:
                dp[i] += (1 + dp[j]) / len(adj_list[i])
    
    return dp[1]

# Sample Input
N = 4
M = 6
passages = [[1, 4], [2, 3], [1, 3], [1, 2], [3, 4], [2, 4]]

print("{:.10f}".format(escape_cave(N, M, passages)) )