def min_unbalancedness(S):
    count_0 = S.count("0")
    count_1 = S.count("1")
    count_q = S.count("?")
    
    min_unbalancedness = abs(count_0 - count_1)
    
    for i in range(count_q + 1):
        unbalancedness = abs(count_1 + i - (count_0 + count_q - i))
        min_unbalancedness = min(min_unbalancedness, unbalancedness)
    
    return min_unbalancedness

S = input()
print(min_unbalancedness(S))