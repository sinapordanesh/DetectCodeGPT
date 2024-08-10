def f(A, B):
    res = ""
    while A > 0 and B > 0:
        if A > B:
            if res[-1:] != "A":
                res += "A"
                A -= 1
            else:
                res += "B"
                B -= 1
        else:
            if res[-1:] != "B":
                res += "B"
                B -= 1
            else:
                res += "A"
                A -= 1
    while A > 0:
        res += "A"
        A -= 1
    while B > 0:
        res += "B"
        B -= 1
    return res

def find_substring(Q, queries):
    for query in queries:
        A, B, C, D = query
        string = f(A, B)
        print(string[C-1:D])

# Sample Input
Q = 5
queries = [(2, 3, 1, 5), (6, 4, 1, 10), (2, 3, 4, 4), (6, 4, 3, 7), (8, 10, 5, 8)]

find_substring(Q, queries)