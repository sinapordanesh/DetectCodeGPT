def boolean_expression_compressor(expression):
    def evaluate(expression):
        stack = []
        for char in expression:
            if char.isalpha():
                stack.append(char)
            elif char == '0' or char == '1':
                stack.append('1')  # Constants evaluate to '1'
            elif char == '-':
                stack.append('1' if stack.pop() == '0' else '0')  # NOT operation
            elif char == '^':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append('1' if operand1 != operand2 else '0')  # XOR operation
            elif char == '*':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append('1' if operand1 == '1' and operand2 == '1' else '0')  # AND operation
        return stack.pop()

    if len(expression) == 1:
        return 1

    min_length = len(expression)
    for i in range(1, len(expression) - 1):
        shortened_expression = expression[:i] + expression[i+1:]
        result = evaluate(shortened_expression)
        if result == evaluate(expression):
            min_length = min(min_length, boolean_expression_compressor(shortened_expression))

    return min_length

while True:
    expression = input()
    if expression == '.':
        break
    print(boolean_expression_compressor(expression))