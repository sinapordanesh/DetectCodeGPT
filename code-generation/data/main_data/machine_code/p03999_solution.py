def evaluate_formulas(S):
    total = int(S)
    n = len(S)
    for i in range(1, n):
        for j in range(i, n):
            left = int(S[:i])
            right = int(S[j:])
            total += left + right
    return total

S = input()
print(evaluate_formulas(S))