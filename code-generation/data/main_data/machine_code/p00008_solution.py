def sum_of_4_integers(n):
    count = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a + b + c + d == n:
                        count += 1
    return count

n = int(input())
print(sum_of_4_integers(n))