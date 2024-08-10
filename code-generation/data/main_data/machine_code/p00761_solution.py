def recurring_decimals(a0, L):
    seen = {}
    a = str(a0).zfill(L)
    count = 0
    while a not in seen:
        seen[a] = count
        min_num = int("".join(sorted(a)))
        max_num = int("".join(sorted(a, reverse=True)))
        a = str(max_num - min_num).zfill(L)
        count += 1
    return seen[a], a, count - seen[a]

# Sample Input
print(recurring_decimals(2012, 4))
print(recurring_decimals(83268, 6))
print(recurring_decimals(1112, 4))
print(recurring_decimals(0, 1))
print(recurring_decimals(99, 2))