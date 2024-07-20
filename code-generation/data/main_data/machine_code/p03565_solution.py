def find_string(S, T):
    for i in range(len(S)-len(T), -1, -1):
        flag = True
        for j in range(len(T)):
            if S[i+j] != '?' and S[i+j] != T[j]:
                flag = False
                break
        if flag:
            new_S = list(S)
            for j in range(len(T)):
                new_S[i+j] = T[j]
            for j in range(len(S)):
                if new_S[j] == '?':
                    new_S[j] = 'a'
            return ''.join(new_S)
    return 'UNRESTORABLE'

# Read input from STDIN
S = input().strip()
T = input().strip()
print(find_string(S, T))