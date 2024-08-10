def number_of_slimes(N, S):
    count = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            count += 1
    return count

N = 10
S = "aabbbbaaca"
print(number_of_slimes(N, S))

N = 5
S = "aaaaa"
print(number_of_slimes(N, S))

N = 20
S = "xxzaffeeeeddfkkkkllq"
print(number_of_slimes(N, S))