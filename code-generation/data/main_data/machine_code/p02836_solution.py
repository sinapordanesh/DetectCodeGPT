def min_hugs_to_palindrome(S):
    n = len(S)
    cnt = 0
    for i in range(n // 2):
        if S[i] != S[n - i - 1]:
            cnt += 1
    return cnt

S = input()
print(min_hugs_to_palindrome(S))