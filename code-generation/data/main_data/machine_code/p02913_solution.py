def max_len_twice_or_more(N, S):
    max_len = 0
    for i in range(1, N):
        for j in range(i+1, N):
            if S[i:i+(j-i)] == S[j:j+(j-i)]:
                max_len = max(max_len, j-i)
    return max_len

N = int(input())
S = input()
print(max_len_twice_or_more(N, S))