from collections import Counter

def get_k(i, j):
    return 2*j - i

if __name__ == '__main__':
    N = int(input())
    S = input()
    C = Counter(S) 
    eq_cnt = 0
    cnt = C['R'] * C['G'] * C['B']
    for i in range(N):
        for j in range(i+1, N):
            k = get_k(i, j)
            if k >= N: continue
            if (S[i] != S[j] and S[i] != S[k] and S[j] != S[k]):
                eq_cnt += 1
    print(cnt - eq_cnt)