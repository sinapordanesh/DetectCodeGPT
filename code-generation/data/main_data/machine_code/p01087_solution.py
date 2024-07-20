def ICPC_calculator():
    while True:
        n = int(input())
        if n == 0:
            break
        
        expression = []
        for _ in range(n):
            expression.append(input())
        
        stack = []
        result = 0
        for line in expression:
            level = line.count('.')
            if line[level] == '+':
                stack.append('+')
            elif line[level] == '*':
                stack.append('*')
            else:
                num = int(line[level:])
                if stack and stack[-1] == '+':
                    result += num
                else:
                    result *= num
        
        print(result)

ICPC_calculator()