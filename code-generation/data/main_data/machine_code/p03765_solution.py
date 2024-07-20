def can_transform(S, T, q, queries):
    def transform_string(string):
        new_string = ""
        i = 0
        while i < len(string):
            if i < len(string)-2 and string[i:i+3] == "AAA":
                i += 3
            elif i < len(string)-2 and string[i:i+3] == "BBB":
                i += 3
            else:
                if string[i] == "A":
                    new_string += "BB"
                else:
                    new_string += "AA"
                i += 1
        return new_string

    for a, b, c, d in queries:
        if transform_string(S[a-1:b]) == T[c-1:d]:
            print("YES")
        else:
            print("NO")

# Sample Input 1
S = "BBBAAAABA"
T = "BBBBA"
q = 4
queries = [(7, 9, 2, 5), (7, 9, 1, 4), (1, 7, 2, 5), (1, 7, 2, 4)]
can_transform(S, T, q, queries)

# Sample Input 2
S = "AAAAABBBBAAABBBBAAAA"
T = "BBBBAAABBBBBBAAAAABB"
q = 10
queries = [(2, 15, 2, 13), (2, 13, 6, 16), (1, 13, 2, 20), (4, 20, 3, 20), (1, 18, 9, 19), 
           (2, 14, 1, 11), (3, 20, 3, 15), (6, 16, 1, 17), (4, 18, 8, 20), (7, 20, 3, 14)]
can_transform(S, T, q, queries)