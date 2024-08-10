def is_palindrome_possible(S, N, operations):
    def apply_operation(char, operation):
        start, end = operation
        if start <= ord(char) - ord("a") + 1 <= end:
            return chr((ord(char) - ord("a") + 1) % 26 + ord("a"))
        return char

    for i in range(N):
        if operations[i][0] == operations[i][1]:
            continue
        S = ''.join([apply_operation(char, operations[i]) for char in S])

    return "YES" if S == S[::-1] else "NO"