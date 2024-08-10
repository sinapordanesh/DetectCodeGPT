from itertools import combinations

def maximize_mean(N, A, B, values):
    max_mean = 0
    count = 0
    
    for i in range(A, B+1):
        for comb in combinations(values, i):
            mean = sum(comb) / len(comb)
            if mean > max_mean:
                max_mean = mean
                count = 1
            elif mean == max_mean:
                count += 1
                
    return '{:.6f}'.format(max_mean), count

# Input
N, A, B = map(int, input().split())
values = list(map(int, input().split()))

# Output
mean, count = maximize_mean(N, A, B, values)
print(mean)
print(count)