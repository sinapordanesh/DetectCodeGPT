def stylish_masters(p, q, P, Q):
    def calculate_indentation(R, C, S, line):
        open_round = line.count('(')
        open_curly = line.count('{')
        open_square = line.count('[')
        close_round = line.count(')')
        close_curly = line.count('}')
        close_square = line.count(']')
        
        return R*(open_round - close_round) + C*(open_curly - close_curly) + S*(open_square - close_square)
    
    R, C, S = None, None, None
    indentations = []
    
    for line in P:
        if '(' in line:
            R = line.index('(')
        elif '{' in line:
            C = line.index('{')
        elif '[' in line:
            S = line.index('[')
    
    for line in Q:
        indentation = calculate_indentation(R, C, S, line)
        if indentation is not None:
            indentations.append(str(indentation))
        else:
            indentations.append("-1")
    
    return " ".join(indentations)