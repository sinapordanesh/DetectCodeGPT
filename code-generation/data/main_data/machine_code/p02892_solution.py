def possible_division(N, S):
    for i in range(N):
        for j in range(i+1, N):
            if S[i][j] == '1' and all(S[i][k] == S[j][k] for k in range(N)):
                return -1
    return N

# Sample Input
N = 2
S = ['01', '10']
print(possible_division(N, S))

N = 3
S = ['011', '101', '110']
print(possible_division(N, S))

N = 6
S = ['010110', '101001', '010100', '101000', '100000', '010000']
print(possible_division(N, S))