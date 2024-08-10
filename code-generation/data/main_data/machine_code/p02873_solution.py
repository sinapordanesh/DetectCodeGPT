def min_sum_good_sequence(S):
    n = len(S) + 1
    ans = n * (n - 1) // 2
    print(ans)
    
min_sum_good_sequence(input().strip())