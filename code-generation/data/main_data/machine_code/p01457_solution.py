def carpenters_language(q, queries):
    S = ""
    result = []
    for i in range(q):
        p, c, n = queries[i]
        S = S[:p] + c*n + S[p:]
        if is_well_formed(S):
            result.append("Yes")
        else:
            result.append("No")
    return result

def is_well_formed(S):
    stack = []
    for char in S:
        if char == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Sample Input 1
q1 = 3
queries1 = [[0, '(', 10], [10, ')', 5], [10, ')', 5]]
print(carpenters_language(q1, queries1))

# Sample Input 2
q2 = 3
queries2 = [[0, ')', 10], [10, '(', 5], [10, '(', 5]]
print(carpenters_language(q2, queries2))

# Sample Input 3
q3 = 3
queries3 = [[0, '(', 10], [10, ')', 20], [0, '(', 10]]
print(carpenters_language(q3, queries3))