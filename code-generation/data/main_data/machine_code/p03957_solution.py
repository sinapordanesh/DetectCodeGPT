def obtain_CF(s):
    if 'C' in s and 'F' in s: 
        index_C = s.index('C')
        index_F = s.index('F', index_C)
        new_s = s[index_C:index_F+1]
        return "Yes" if new_s == 'CF' else "No"
    else:
        return "No" 

# Test cases
print(obtain_CF("CODEFESTIVAL"))
print(obtain_CF("FESTIVALCODE"))
print(obtain_CF("CF"))
print(obtain_CF("FCF"))