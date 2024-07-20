def change_password(S):
    lst = list(S)
    lst.sort(reverse=True)
    if lst[0] == '0':
        lst[0], lst[1] = lst[1], lst[0]
    
    return ''.join(lst)

# Sample Test Cases
print(change_password("201")) # 701
print(change_password("512")) # 012
print(change_password("99999")) # 49876
print(change_password("765876346")) # 26587493