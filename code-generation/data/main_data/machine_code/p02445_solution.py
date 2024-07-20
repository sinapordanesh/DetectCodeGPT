def swap_elements(n, arr, queries):
    for b, e, t in queries:
        for k in range(e - b):
            arr[b + k], arr[t + k] = arr[t + k], arr[b + k]
    
    return arr

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = []
for _ in range(q):
    queries.append(tuple(map(int, input().split())))

result = swap_elements(n, arr, queries)
print(*result)