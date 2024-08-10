def min_amount_of_money_needed(A, B, C, X, Y):
    min_money = float('inf')
    for i in range(max(X, Y) + 1):
        total_money = i * 2 * C + max(0, X - i) * A + max(0, Y - i) * B
        min_money = min(min_money, total_money)
    return min_money

A, B, C, X, Y = map(int, input().split())
print(min_amount_of_money_needed(A, B, C, X, Y))