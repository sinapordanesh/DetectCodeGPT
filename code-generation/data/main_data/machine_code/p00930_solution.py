def flipping_parentheses(N, Q, s, queries):
    def balanced_state(s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        return set(stack)
    
    def flip_parentheses(position, balanced_positions):
        if position in balanced_positions:
            balanced_positions.remove(position)
        elif len(balanced_positions) > 0:
            balanced_positions.add(position)
        return balanced_positions
    
    balanced_positions = balanced_state(s)
    result = []
    
    for query in queries:
        balanced_positions = flip_parentheses(query-1, balanced_positions)
        result.append(min(balanced_positions) + 1)
    
    return result

# Sample Input 1
N1 = 6
Q1 = 3
s1 = "((()))"
queries1 = [4, 3, 1]
print(flipping_parentheses(N1, Q1, s1, queries1))

# Sample Input 2
N2 = 20
Q2 = 9
s2 = "()((((()))))()()()()"
queries2 = [15, 20, 13, 5, 3, 10, 3, 17, 18]
print(flipping_parentheses(N2, Q2, s2, queries2) )