def evaluate_possible_formulas(S):
    def backtrack(s, idx, expression):
        nonlocal total
        if idx == len(s):
            total += eval(expression)
            return
        if idx == 0:
            backtrack(s, idx + 1, expression + s[idx])
        else:
            backtrack(s, idx + 1, expression + '+' + s[idx])
            backtrack(s, idx + 1, expression + s[idx])
    
    total = 0
    backtrack(S, 0, '')
    return total

# Input
S = "125"

# Output
print(evaluate_possible_formulas(S))