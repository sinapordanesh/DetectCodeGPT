def additions(N, S):
    def calculate(expr):
        try:
            return eval(expr)
        except:
            return float('inf')
    
    if '+' not in S:
        return 0 if int(S) <= N else -1
    
    min_replaced = float('inf')
    
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            new_expr = S[:i] + '+' + S[i+1:j] + '+' + S[j:]
            replaced = len(S) - len(new_expr)
            if replaced >= min_replaced:
                continue
            if calculate(new_expr) <= N:
                min_replaced = replaced
    
    return min_replaced if min_replaced != float('inf') else -1