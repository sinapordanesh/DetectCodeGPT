def is_last_day_of_month(M1, D1, M2, D2):
    if D1 == 30 or (M1 in [4, 6, 9, 11] and D1 == 30) or (M1 == 2 and D1 == 28):
        return 1
    else:
        return 0

# Sample Input 1
# M1, D1, M2, D2 = 11, 16, 11, 17
# print(is_last_day_of_month(M1, D1, M2, D2))

# Sample Input 2
# M1, D1, M2, D2 = 11, 30, 12, 1
# print(is_last_day_of_month(M1, D1, M2, D2))