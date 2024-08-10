def good_sub_grids(n, m):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(i, n+1):
                for l in range(j, n+1):
                    total = 0
                    for x in range(i, k+1):
                        for y in range(j, l+1):
                            total += ((x-1)*n + y)
                    if total == m:
                        count += 1
    return count

print(good_sub_grids(7, 7))
print(good_sub_grids(6, 0))
print(good_sub_grids(18, 10))