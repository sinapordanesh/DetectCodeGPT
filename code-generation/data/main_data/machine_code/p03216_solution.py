def calculate_DMC_number(N, S, Q, k_values):
    def count_triplets(S, k):
        count = 0
        for a in range(len(S)):
            if S[a] == 'D':
                for b in range(a+1, len(S)):
                    if S[b] == 'M':
                        for c in range(b+1, len(S)):
                            if S[c] == 'C' and c - a < k:
                                count += 1
        return count
    
    for k in k_values:
        print(count_triplets(S, k))