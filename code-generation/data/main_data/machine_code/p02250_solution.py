def string_search(T, Q, queries):
    for query in queries:
        if query in T:
            print(1)
        else:
            print(0)

# Sample Input
T = "aabaaa"
Q = 4
queries = ["aa", "ba", "bb", "xyz"]

string_search(T, Q, queries)