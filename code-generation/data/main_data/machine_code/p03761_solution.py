def longest_common_string(n, strings):
    from collections import Counter
    counts = [Counter(s) for s in strings]
    common = counts[0]
    for i in range(1, n):
        common &= counts[i]
    
    result = []
    for char, count in sorted(common.items()):
        result.append(char * count)
    
    return ''.join(result)

# Sample Input
n = 3
strings = ['cbaa', 'daacc', 'acacac']
print(longest_common_string(n, strings))

n = 3
strings = ['a', 'aa', 'b']
print(longest_common_string(n, strings) )