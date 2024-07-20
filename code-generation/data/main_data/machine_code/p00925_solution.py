def check_rule(expression, answer):
    def evaluate(expr):
        stack = []
        i = 0
        while i < len(expr):
            if expr[i].isdigit():
                stack.append(int(expr[i]))
            else:
                if expr[i] == '*':
                    a = stack.pop()
                    b = int(expr[i + 1])
                    stack.append(a * b)
                    i += 1
            i += 1
        return sum(stack)

    if evaluate(expression) == answer:
        return 'L'
    elif eval(expression) == answer:
        return 'M'
    elif evaluate(expression) == answer and eval(expression) == answer:
        return 'U'
    else:
        return 'I'