def max_sum_of_cards(A, B, C, K):
    if K <= A:
        return K
    elif K <= A + B:
        return A
    else:
        return A - (K - A - B) 

A, B, C, K = map(int, input().split())
print(max_sum_of_cards(A, B, C, K))