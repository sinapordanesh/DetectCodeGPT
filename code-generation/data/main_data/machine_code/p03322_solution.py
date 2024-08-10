def possible_pairs(N, S):
    cnt = 0
    for i in range(N):
        plus = 0
        minus = 0
        greater = 0
        lesser = 0
        for j in range(i, N):
            if S[j] == '+':
                plus += 1
            elif S[j] == '-':
                minus += 1
            elif S[j] == '>':
                greater += 1
            elif S[j] == '<':
                lesser += 1
            if plus - minus == 1 and greater - lesser == 0:
                cnt += 1
    return cnt

N = int(input())
S = input().strip()
print(possible_pairs(N, S))