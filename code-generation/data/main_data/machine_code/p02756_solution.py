def final_string(S, Q, queries):
    for query in queries:
        if query[0] == 1:
            S = S[::-1]
        elif query[0] == 2:
            if query[1] == 1:
                S = query[2] + S
            elif query[1] == 2:
                S = S + query[2]
    return S

# Sample Input 1
S = "a"
Q = 4
queries = [[2, 1, "p"], [1], [2, 2, "c"], [1]]
print(final_string(S, Q, queries))

# Sample Input 2
S = "a"
Q = 6
queries = [[2, 2, "a"], [2, 1, "b"], [1], [2, 2, "c"], [1], [1]]
print(final_string(S, Q, queries))

# Sample Input 3
S = "y"
Q = 1
queries = [[2, 1, "x"]]
print(final_string(S, Q, queries))