def concatenate_letters(S, w):
    result = ''
    for i in range(0, len(S), w):
        result += S[i]
    return result

S = input()
w = int(input())
print(concatenate_letters(S, w))