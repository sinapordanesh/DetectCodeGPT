def daves_string(A):
    if A % 2 == 1:
        return '(' + ')' * (A // 2) + '('
    else:
        return ')' * (A // 2) + '(' + ')' * (A // 2)