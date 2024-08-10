def people_at_theater(N, seats):
    total_people = 0
    for seat_range in seats:
        total_people += seat_range[1] - seat_range[0] + 1
    return total_people

# Sample Input 1
print(people_at_theater(1, [(24, 30)]))

# Sample Input 2
print(people_at_theater(2, [(6, 8), (3, 3)]) )