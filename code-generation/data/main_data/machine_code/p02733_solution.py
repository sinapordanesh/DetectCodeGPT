def chocolate_cut(H, W, K, S):
    def count_white(s):
        return sum(1 for i in range(W) if s[i] == '1')
    
    total_cuts = 0
    for i in range(1 << (H - 1)):
        cuts = bin(i).count('1')
        blocks = [S[j:(j + W)] for j in range(0, H * W, W)]
        temp_cuts = cuts
        
        for j in range(1, H):
            if (i >> (j - 1)) & 1:
                temp_row = [0] * W
                for m in range(j):
                    for n in range(W):
                        temp_row[n] += int(blocks[m][n])
                if max(temp_row) > K:
                    temp_cuts = float('inf')
                    break
                else:
                    temp_cuts += 1
                    temp_row = [0] * W
                
        total_cuts = min(total_cuts, temp_cuts)
    
    return total_cuts

# Sample Input 1
print(chocolate_cut(3, 5, 4, ["11100", "10001", "00111"])) # 2

# Sample Input 2
print(chocolate_cut(3, 5, 8, ["11100", "10001", "00111"])) # 0

# Sample Input 3
print(chocolate_cut(4, 10, 4, ["1110010010", "1000101110", "0011101001", "1101000111"])) # 3