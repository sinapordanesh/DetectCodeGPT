def count_integers(N, K):
    count = 0
    for i in range(1, N+1):
        if str(i).count('0') + str(i).count('1') + str(i).count('2') + str(i).count('3') == K:
            count += 1
    return count

# Sample Input 1
print(count_integers(100, 1))

# Sample Input 2
print(count_integers(25, 2))

# Sample Input 3
print(count_integers(314159, 2))

# Sample Input 4
print(count_integers(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 3))