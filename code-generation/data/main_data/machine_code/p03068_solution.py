def replace_characters(N, S, K):
    result = ""
    for i in range(N):
        if S[i] != S[K-1]:
            result += "*"
        else:
            result += S[i]
    return result

N = int(input())
S = input()
K = int(input())
print(replace_characters(N, S, K))