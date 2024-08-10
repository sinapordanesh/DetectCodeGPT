def max_integer(S):
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
    return min(len(S), count*2)

# Sample Input 1
print(max_integer("010"))

# Sample Input 2
print(max_integer("100000000"))

# Sample Input 3
print(max_integer("00001111"))