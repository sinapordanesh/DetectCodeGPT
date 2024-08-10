def compute_area(d):
    total_area = 0
    for i in range(d, 600, d):
        total_area += i**2 * d
    return total_area

# Input
datasets = [20, 10]

# Output
for d in datasets:
    print(compute_area(d))