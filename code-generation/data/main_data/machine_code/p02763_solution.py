def process_queries(N, S, Q, queries):
    unique_chars = set(S)
    for query in queries:
        if query[0] == 1:
            i_q, c_q = query[1:]
            if S[i_q-1] != c_q:
                S = S[:i_q-1] + c_q + S[i_q:]
                unique_chars.add(c_q)
        elif query[0] == 2:
            l_q, r_q = query[1:]
            substring = S[l_q-1:r_q]
            unique_chars_in_substring = set(substring)
            print(len(unique_chars_in_substring))

# Sample Input
N = 7
S = "abcdbbd"
Q = 6
queries = [
    [2, 3, 6],
    [1, 5, 'z'],
    [2, 1, 1],
    [1, 4, 'a'],
    [1, 7, 'd'],
    [2, 1, 7]
]

process_queries(N, S, Q, queries)