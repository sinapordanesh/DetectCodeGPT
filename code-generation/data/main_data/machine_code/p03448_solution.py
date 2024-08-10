def count_coin_combinations(A, B, C, X):
    count = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                total = a*500 + b*100 + c*50
                if total == X:
                    count += 1
    return count

A, B, C, X = map(int, input().split())
print(count_coin_combinations(A, B, C, X))