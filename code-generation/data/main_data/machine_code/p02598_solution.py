import math

def shortest_longest_log_length(N, K, logs):
    left = 1
    right = max(logs)
    
    while left < right:
        mid = (left + right) // 2
        cuts = sum(math.ceil(log / mid) - 1 for log in logs)
        
        if cuts <= K:
            right = mid
        else:
            left = mid + 1
            
    return math.ceil(right)

# Sample Input 1
print(shortest_longest_log_length(2, 3, [7, 9])) # 4

# Sample Input 2
print(shortest_longest_log_length(3, 0, [3, 4, 5])) # 5

# Sample Input 3
print(shortest_longest_log_length(10, 10, [158260522, 877914575, 602436426, 24979445, 861648772, 623690081, 433933447, 476190629, 262703497, 211047202])) # 292638192