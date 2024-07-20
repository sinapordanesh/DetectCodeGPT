def count_rectangular_regions(S):
    count = 0
    for a in range(1, S+1):
        for b in range(a, S+1):
            if (S % (b-a+1) == 0):
                count += 1
    return count

S = int(input())
print(count_rectangular_regions(S))