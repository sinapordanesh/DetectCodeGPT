def max_jewels(N, arr, M, conditions):
    max_value = 0
    for condition in conditions:
        t, a, b = condition
        if t == 'L':
            valid_jewels = [j for j in arr if j[0] <= a]
        elif t == 'R':
            valid_jewels = [j for j in arr if j[0] >= a]
        elif t == 'D':
            valid_jewels = [j for j in arr if j[1] <= a]
        elif t == 'U':
            valid_jewels = [j for j in arr if j[1] >= a]
        
        valid_jewels.sort(key=lambda x: x[2], reverse=True)
        count = 0
        value = 0
        for jewel in valid_jewels:
            if count == b:
                break
            value += jewel[2]
            count += 1
        max_value += value
        
    return max_value

# Input
N = int(input())
arr = []
for _ in range(N):
    x, y, v = map(int, input().split())
    arr.append((x, y, v))
M = int(input())
conditions = []
for _ in range(M):
    t, a, b = input().split()
    conditions.append((t, int(a), int(b)))

# Calculate and output result
print(max_jewels(N, arr, M, conditions))