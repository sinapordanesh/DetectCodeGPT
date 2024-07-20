def calculate_set_expression(sets, expression):
    def union(A, B):
        return A.union(B)
    
    def intersection(A, B):
        return A.intersection(B)
    
    def difference(A, B):
        return A.difference(B)
    
    def symmetric_difference(A, B):
        return A.symmetric_difference(B)
    
    def complement(A, U):
        return U.difference(A)
    
    sets_dict = {}
    for set_name, set_elements in sets:
        sets_dict[set_name] = set(set_elements)
    
    U = set().union(*sets_dict.values())
    
    stack = []
    for char in expression:
        if char.isalpha():
            stack.append(sets_dict[char])
        elif char == 'c':
            A = stack.pop()
            stack.append(complement(A, U))
        else:
            B = stack.pop()
            A = stack.pop()
            if char == 'u':
                stack.append(union(A, B))
            elif char == 'i':
                stack.append(intersection(A, B))
            elif char == 'd':
                stack.append(difference(A, B))
            elif char == 's':
                stack.append(symmetric_difference(A, B))
    
    result = stack.pop()
    if len(result) == 0:
        return "NULL"
    return " ".join(map(str, sorted(result)))

# Sample Input
sets = [("A", [1, 3, -1]), ("B", [3, 1, 5, 7]), ("D", [5])]
expression = "cAiBdD"
print(calculate_set_expression(sets, expression))

sets = [("C", [1, 2, 3]), ("A", [2, 10, 8, 3]), ("B", [2, 4, 8])]
expression = "(As(AiB))uC"
print(calculate_set_expression(sets, expression))