def is_back_home(S):
    x = S.count('S') - S.count('N')
    y = S.count('E') - S.count('W')
    
    if x == 0 and y == 0:
        return 'Yes'
    else:
        return 'No'