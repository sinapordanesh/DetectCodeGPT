def evaluate_formula(formula):
    def evaluate_helper(formula, P, Q, R):
        if formula == '0':
            return 0
        elif formula == '1':
            return 1
        elif formula == '2':
            return 2
        elif formula == 'P':
            return P
        elif formula == 'Q':
            return Q
        elif formula == 'R':
            return R
        elif formula[0] == '-':
            return 2 - evaluate_helper(formula[1], P, Q, R)
        elif formula[0] == '(' and formula[-1] == ')':
            op = formula[1]
            if op == '*':
                return min(evaluate_helper(formula[2:formula.index('*')], P, Q, R), evaluate_helper(formula[formula.index('*')+1:-1], P, Q, R))
            elif op == '+':
                return max(evaluate_helper(formula[2:formula.index('+')], P, Q, R), evaluate_helper(formula[formula.index('+')+1:-1], P, Q, R))
    for line in formula:
        if line == '.':
            break
        P, Q, R = 0, 0, 0
        count = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if evaluate_helper(line, i, j, k) == 2:
                        count += 1
        print(count)