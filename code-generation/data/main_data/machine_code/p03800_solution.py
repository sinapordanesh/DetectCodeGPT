def assign_species(N, s):
    ans = ['S'] * N
    for i in range(N):
        if s[i] == 'x':
            if ans[i] == 'S':
                ans[i] = 'W'
            else:
                ans[i] = 'S'
                
            if i > 0:
                if ans[i-1] == ans[i]:
                    if ans[i] == 'S':
                        ans[i] = 'W'
                    else:
                        ans[i] = 'S'
            
            if i < N-1:
                if ans[i+1] == ans[i]:
                    if ans[i] == 'S':
                        ans[i] = 'W'
                    else:
                        ans[i] = 'S'
    
    if s[0] == 'o':
        if ans[0] != ans[N-1] and ans[0] == ans[1]:
            return ''.join(ans)
        else:
            return -1
    else:
        if ans[0] != ans[N-1] and ans[0] != ans[1]:
            return ''.join(ans)
        else:
            return -1

# Sample Input 1
print(assign_species(6, 'ooxoox'))

# Sample Input 2
print(assign_species(3, 'oox'))

# Sample Input 3
print(assign_species(10, 'oxooxoxoox'))