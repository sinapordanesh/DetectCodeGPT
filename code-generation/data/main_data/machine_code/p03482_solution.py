def max_integer(S):
    ones_count = S.count("1")
    return min(ones_count, len(S) - ones_count)

S = input()
print(max_integer(S))