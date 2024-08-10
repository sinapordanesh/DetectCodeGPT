def max_evaluated_value(N, formula):
    ans = 0
    signs = []
    
    for i in range(N):
        if formula[i] == '+':
            signs.append(1)
        else:
            signs.append(-1)
    
    cumulative_sum = [0] * (N+1)
    for i in range(N):
        cumulative_sum[i+1] = cumulative_sum[i] + signs[i]
    
    min_val = float('inf')
    ans = 0
    for i in range(1, N):
        ans = max(ans, cumulative_sum[i] - min_val)
        min_val = min(min_val, cumulative_sum[i])
    
    return ans + cumulative_sum[N] 

# Input
N = int(input())
formula = input().split()

# Output
print(max_evaluated_value(N, formula))