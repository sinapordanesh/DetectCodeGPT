def atcoder_mart(X):
    items = [100, 101, 102, 103, 104, 105]
    
    for i in range(2**6):
        total_cost = 0
        for j in range(6):
            if (i >> j) & 1:
                total_cost += items[j]
        
        if total_cost == X:
            return 1
    
    return 0

# Sample Input 1
print(atcoder_mart(615))

# Sample Input 2
print(atcoder_mart(217))