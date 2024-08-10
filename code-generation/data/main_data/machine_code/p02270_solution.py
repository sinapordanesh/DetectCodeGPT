def check_truck_capacity(n, k, weights):
    left = max(weights)
    right = sum(weights)
    
    while left < right:
        mid = (left + right) // 2
        current_weight = 0
        trucks_needed = 1
        
        for weight in weights:
            if current_weight + weight <= mid:
                current_weight += weight
            else:
                current_weight = weight
                trucks_needed += 1
        
        if trucks_needed <= k:
            right = mid
        else:
            left = mid + 1
    
    return left

# Read input values
n, k = map(int, input().split())
weights = [int(input()) for _ in range(n)]

# Call the function and print the result
print(check_truck_capacity(n, k, weights))