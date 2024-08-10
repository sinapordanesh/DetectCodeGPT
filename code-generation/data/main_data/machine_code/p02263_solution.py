def reverse_polish_notation(expression):
    stack = []
    operators = set(['+', '-', '*'])
    
    for symbol in expression.split():
        if symbol not in operators:
            stack.append(int(symbol))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if symbol == '+':
                stack.append(operand1 + operand2)
            elif symbol == '-':
                stack.append(operand1 - operand2)
            elif symbol == '*':
                stack.append(operand1 * operand2)
    
    return stack[0]

# Sample Input 1
print(reverse_polish_notation("1 2 +"))

# Sample Input 2
print(reverse_polish_notation("1 2 + 3 4 - *"))