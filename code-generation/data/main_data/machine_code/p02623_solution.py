def max_books(N, M, K, A, B):
    total_time = 0
    num_books = 0
    i = 0
    j = 0
    
    while i < N and total_time + A[i] <= K:
        total_time += A[i]
        num_books += 1
        i += 1
        
    while j < M and i >= 0:
        total_time += B[j]
        j += 1
        while total_time > K and i > 0:
            i -= 1
            total_time -= A[i]
            
        if total_time <= K:
            num_books = max(num_books, i+j)
    
    return num_books

# Input
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Output
print(max_books(N, M, K, A, B))