def lexicographically_smallest_string(N, L, strings):
    strings.sort()
    return ''.join(strings)

# Sample Input
N = 3
L = 3
strings = ['dxx', 'axx', 'cxx']

print(lexicographically_smallest_string(N, L, strings))