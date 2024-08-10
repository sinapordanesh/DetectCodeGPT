def min_money_needed(N, A):
    total = sum(A)
    prev = 0
    ans = float('inf')
    
    for i in range(N-1):
        prev += A[i]
        rest = total - prev
        ans = min(ans, abs(prev - rest))
    
    return ans

# Sample Input 1
# N = 3
# A = [2, 4, 3]
# Sample Output 1
# min_money_needed(N, A)

# Sample Input 2
# N = 12
# A = [100, 104, 102, 105, 103, 103, 101, 105, 104, 102, 104, 101]
# Sample Output 2
# min_money_needed(N, A)