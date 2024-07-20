def min_total_stamina(N, X):
    total_stamina = 0
    for i in range(1, 101):
        stamina = sum([(x - i)**2 for x in X])
        total_stamina = min(total_stamina, stamina) if total_stamina != 0 else stamina
    return total_stamina

# Sample Input 1
print(min_total_stamina(2, [1, 4]))

# Sample Input 2
print(min_total_stamina(7, [14, 14, 2, 13, 56, 2, 37]))