def sum_ABC_numbers(S):
    Q = S.count("?")
    total_sum = 0
    for i in range(3**Q):
        new_S = S.replace("?", "A", i // (3**(Q-1)) % 3)
        new_S = new_S.replace("?", "B", i // (3**(Q-2)) % 3)
        new_S = new_S.replace("?", "C", i % 3)
        
        count = 0
        for j in range(len(new_S)):
            if new_S[j] == "A":
                for k in range(j+1, len(new_S)):
                    if new_S[k] == "B":
                        count += new_S[k+1:].count("C")
        
        total_sum += count
    
    return total_sum % (10**9 + 7)