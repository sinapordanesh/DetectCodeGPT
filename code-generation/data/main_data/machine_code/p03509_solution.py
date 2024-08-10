def min_members_to_pass_bill(N, P, members):
    total_white_ballots = sum([member[0] for member in members])
    threshold = (P * sum([member[0] + member[1] for member in members]) + 99) // 100
    required_white_ballots = max(0, threshold - total_white_ballots)
    count = 0
    for member in members:
        if member[0] >= required_white_ballots:
            count += 1
    return count

# Sample Input 1
print(min_members_to_pass_bill(4, 75, [(1, 1), (1, 1), (1, 1), (1, 1)]))

# Sample Input 2
print(min_members_to_pass_bill(4, 75, [(1, 1), (1, 1), (1, 1), (100, 1)]))

# Sample Input 3
print(min_members_to_pass_bill(5, 60, [(6, 3), (5, 9), (3, 4), (7, 8), (4, 7)]))