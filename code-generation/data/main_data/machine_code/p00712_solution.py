def unit_fraction_partition(p, q, a, n):
    if p == 0 and q == 0 and a == 0 and n == 0:
        return 0
    return 0

print(unit_fraction_partition(2, 3, 120, 3))
print(unit_fraction_partition(2, 3, 300, 3))
print(unit_fraction_partition(2, 3, 299, 3))
print(unit_fraction_partition(2, 3, 12, 3))
print(unit_fraction_partition(2, 3, 12000, 7))
print(unit_fraction_partition(54, 795, 12000, 7))
print(unit_fraction_partition(2, 3, 300, 1))
print(unit_fraction_partition(2, 1, 200, 5))
print(unit_fraction_partition(2, 4, 54, 2))