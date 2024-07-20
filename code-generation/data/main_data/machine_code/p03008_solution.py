def max_acorns(N, g_A, s_A, b_A, g_B, s_B, b_B):
    max_acorns = N
    
    gold_A = N // g_A
    silver_A = gold_A
    bronze_A = gold_A
    
    acorns_after_A = N % g_A
    acorns_after_B = (gold_A * g_A) // g_B
    
    max_acorns = max(max_acorns, (acorns_after_A + acorns_after_B))
    
    return max_acorns

#Sample Input
N = 23
g_A = 1
s_A = 1
b_A = 1
g_B = 2
s_B = 1
b_B = 1

print(max_acorns(N, g_A, s_A, b_A, g_B, s_B, b_B))