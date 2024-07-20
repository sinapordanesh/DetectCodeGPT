def balance_of_world(input_string):
    stack = []
    for char in input_string:
        if char in '([':
            stack.append(char)
        elif char == ')' and (not stack or stack.pop() != '('):
            return 'no'
        elif char == ']' and (not stack or stack.pop() != '['):
            return 'no'
    return 'yes' if not stack else 'no'