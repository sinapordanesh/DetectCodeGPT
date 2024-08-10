def device_state(N, K, S):
    for _ in range(K):
        new_S = ''
        for i in range(N):
            if S[i] == 'A':
                if i == 0:
                    if S[i+1] == 'A':
                        new_S += 'B'
                    else:
                        new_S += 'A'
                elif i == N-1:
                    if S[i-1] == 'A':
                        new_S += 'B'
                    else:
                        new_S += 'A'
                else:
                    if S[i-1] == 'A' or S[i+1] == 'A':
                        new_S += 'B'
                    else:
                        new_S += 'A'
            else:
                if i == 0:
                    if S[i+1] == 'A':
                        new_S += 'A'
                    else:
                        new_S += 'B'
                elif i == N-1:
                    if S[i-1] == 'A':
                        new_S += 'A'
                    else:
                        new_S += 'B'
                else:
                    if S[i-1] == 'A' or S[i+1] == 'A':
                        new_S += 'A'
                    else:
                        new_S += 'B'
        S = new_S
    return S

N, K, S = map(str, input().split())
print(device_state(int(N), int(K), S))