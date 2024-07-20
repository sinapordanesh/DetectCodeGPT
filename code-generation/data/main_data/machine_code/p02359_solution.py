def max_customers(N, T, intervals):
    events = []
    for l, r in intervals:
        events.append((l, 1))
        events.append((r, -1))
    
    events.sort()
    
    max_customers = 0
    current_customers = 0
    
    for event in events:
        current_customers += event[1]
        max_customers = max(max_customers, current_customers)
    
    return max_customers

# Sample Input
N = 6
T = 10
intervals = [(0, 2), (1, 3), (2, 6), (3, 8), (4, 10), (5, 10)]
print(max_customers(N, T, intervals))

N = 2
T = 2
intervals = [(0, 1), (1, 2)]
print(max_customers(N, T, intervals))