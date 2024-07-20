def process_expression(expression):
    operation = expression.find('@')
    if operation == -1:
        if expression[0] == '(':
            return expression[1:-1]
        else:
            return expression
    if expression[0] == '(':
        if expression[operation + 1] == '(':
            return process_expression(expression[1:operation]) + process_expression(expression[operation + 1:-1])
        else:
            return process_expression(expression[1:operation]) + expression[operation]
    else:
        if expression[operation + 1] == '(':
            return expression[0:operation + 1] + process_expression(expression[operation + 1:-1])
        else:
            return expression[0:operation + 1] + expression[operation + 1:]

def find_treasure(dataset):
    treasure = process_expression(dataset)
    if '(' in treasure:
        treasure = eval(treasure)
    return treasure

while True:
    dataset = input()
    if dataset == "#":
        break
    result = find_treasure(dataset)
    print("{:.8f} {:.8f}".format(result[0], result[1]) if type(result) == tuple else result)