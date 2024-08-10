def string_sequence(N, strings, Q, queries):
    def string_key(string, perm):
        key = {char: perm.index(char) for char in string}
        return tuple(key[char] for char in string)
    
    sorted_strings = sorted(strings, key=lambda x: string_key(x, 'abcdefghijklmnopqrstuvwxyz'))
    
    result = []
    for query in queries:
        k, perm = query
        index = sorted_strings.index(strings[k-1]) + 1
        result.append(index)
    
    return result

N = 5
strings = ['aa', 'abbaa', 'abbba', 'aaab', 'aaaaaba']
Q = 5
queries = [(1, 'abcdefghijklmnopqrstuvwxyz'), (2, 'bacdefghijklmnopqrstuvwxyz'), 
           (3, 'abcdefghijklmnopqrstuvwxyz'), (4, 'bacdefghijklmnopqrstuvwxyz'), 
           (5, 'abcdefghijklmnopqrstuvwxyz')]

print(*string_sequence(N, strings, Q, queries), sep='\n')