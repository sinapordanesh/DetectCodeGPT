def min_operations(N, p):
    count = 0
    for i in range(N):
        if p[i] == i+1:
            count += 1
    return (count + 1) // 2

# Read input
N = int(input())
p = list(map(int, input().split()))

# Print output
print(min_operations(N, p))