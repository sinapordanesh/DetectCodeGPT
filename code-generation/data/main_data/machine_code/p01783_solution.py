def D_LR(s):
    def eval_expr(expr):
        if 'L' not in expr and 'R' not in expr:
            return int(expr)
        else:
            for i in range(len(expr)):
                if expr[i] == 'R':
                    return eval_expr(expr[i+1:]) if expr[i+1] != 'L' else eval_expr(expr[i+1:len(expr)-1])
                elif expr[i] == 'L':
                    return eval_expr(expr[i+1:])
    
    max_score = 0
    nums = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(10):
        expr = s.replace('?', str(i))
        if expr[0] == '0':
            continue
        try:
            score = eval_expr(expr)
            max_score = max(max_score, score)
        except:
            continue
    
    if max_score == 0:
        print("invalid")
    else:
        print(max_score)

s = input().strip()
D_LR(s)