def evaluate_expression(expression):
    return str(eval(expression.replace('^','**')).split('.')[0])

n = int(input())
for _ in range(n):
    exp = input().strip('=')    
    print(evaluate_expression(exp))