def repeated_substitution(n, pairs, initial, final):
    def substitute(input_str, alpha, beta):
        while alpha in input_str:
            input_str = input_str.replace(alpha, beta)
        return input_str

    substitutions = {pair[0]: pair[1] for pair in pairs}
    num_substitutions = 0
    current_str = initial

    while current_str != final:
        if num_substitutions > 10:
            return -1
        for alpha, beta in substitutions.items():
            result = substitute(current_str, alpha, beta)
            if result != current_str:
                current_str = result
                num_substitutions += 1
                break

    return num_substitutions

print(repeated_substitution(2, [('a', 'bb'), ('b', 'aa')], 'a', 'bbbbbbbb'))
print(repeated_substitution(1, [('a', 'aa')], 'a', 'aaaaa'))
print(repeated_substitution(3, [('ab', 'aab'), ('abc', 'aadc'), ('ad', 'dee')], 'abc', 'deeeeeeeec'))
print(repeated_substitution(10, [('a', 'abc'), ('b', 'bai'), ('c', 'acf'), ('d', 'bed'), ('e', 'abh'), ('f', 'fag'), ('g', 'abe'), ('h', 'bag'), ('i', 'aaj'), ('j', 'bbb')], 'a', 'abacfaabe'))