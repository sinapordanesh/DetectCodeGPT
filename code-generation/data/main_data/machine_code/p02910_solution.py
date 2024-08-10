def is_easily_playable(S):
    for i in range(len(S)):
        if (i+1) % 2 != 0 and S[i] not in ['R', 'U', 'D']:
            return "No"
        elif (i+1) % 2 == 0 and S[i] not in ['L', 'U', 'D']:
            return "No"
    return "Yes" 

S = input()
print(is_easily_playable(S))