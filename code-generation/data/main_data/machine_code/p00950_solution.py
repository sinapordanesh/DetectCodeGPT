def possible_equations(s):
    from itertools import permutations
    
    def evaluate(equation):
        values = []
        for c in equation:
            if c == '0':
                values.append(0)
            elif c == '1':
                values.append(1)
            elif c == '-':
                values[-1] *= -1
            elif c == '*':
                values[-1] *= values.pop()
            elif c == '+':
                continue
        return sum(values)
    
    unique_chars = set([char for char in s if char.isalpha()])
    unique_chars_num = len(unique_chars)
    possible_equations = 0
    
    for perm in permutations(range(10), unique_chars_num):
        mapping = dict(zip(unique_chars, perm))
        equation = ''.join([str(mapping[char]) if char.isalpha() else char for char in s])
        if evaluate(equation[:equation.index('=')]) == evaluate(equation[equation.index('=')+1:]):
            possible_equations += 1
            
    return possible_equations

# Test cases
print(possible_equations("ACM"))
print(possible_equations("icpc"))
print(possible_equations("BAYL0R"))
print(possible_equations("-AB+AC-A"))
print(possible_equations("abcdefghi"))
print(possible_equations("111-10=1+10*10"))
print(possible_equations("0=10-1"))