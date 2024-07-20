def evaluate_formula():
    formula = input().split()
    A = int(formula[0])
    op = formula[1]
    B = int(formula[2])
    
    if op == '+':
        print(A + B)
    elif op == '-':
        print(A - B)

evaluate_formula()