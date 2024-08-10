def count_AC_substring(N, Q, S, queries):
    result = []
    for query in queries:
        l, r = query
        substring = S[l-1:r]
        count = 0
        for i in range(len(substring)-1):
            if substring[i:i+2] == 'AC':
                count += 1
        result.append(count)
    return result

# Sample Input
N = 8
Q = 3
S = "ACACTACG"
queries = [(3, 7), (2, 3), (1, 8)]

# Sample Output
print(*count_AC_substring(N, Q, S, queries), sep="\n")