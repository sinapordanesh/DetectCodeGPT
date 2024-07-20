def remove_leaves(H, W, pond):
    s_row, s_col = -1, -1
    t_row, t_col = -1, -1
    leaves = 0
    
    for i in range(H):
        for j in range(W):
            if pond[i][j] == 'S':
                s_row, s_col = i, j
            elif pond[i][j] == 'T':
                t_row, t_col = i, j
            elif pond[i][j] == 'o':
                leaves += 1
    
    if s_row == t_row or s_col == t_col:
        return max(0, leaves - 1)
    else:
        return max(0, leaves)

# Sample Input 1
print(remove_leaves(3, 3, ['S.o', '.o.', 'o.T']))

# Sample Input 2
print(remove_leaves(3, 4, ['S...', '.oo.', '...T']))

# Sample Input 3
print(remove_leaves(4, 3, ['.S.', '.o.', '.o.', '.T.']))

# Sample Input 4
print(remove_leaves(10, 10, ['.o...o..o.', '....o.....', '....oo.oo.', '..oooo..o.', '....oo....', '..o..o....', 'o..o....So', 'o....T....', '....o.....', '........oo']))