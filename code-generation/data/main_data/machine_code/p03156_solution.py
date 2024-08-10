def max_contests(N, A, B, scores):
    scores.sort()
    count = 0
    used = []
    for i in range(N):
        if scores[i] <= A and 'A' not in used:
            count += 1
            used.append('A')
        elif A < scores[i] <= B and 'B' not in used:
            count += 1
            used.append('B')
        elif scores[i] > B and 'C' not in used:
            count += 1
            used.append('C')
    return count

# Sample Input 1
print(max_contests(7, 5, 15, [1, 10, 16, 2, 7, 20, 12]))

# Sample Input 2
print(max_contests(8, 3, 8, [5, 5, 5, 10, 10, 10, 15, 20]))

# Sample Input 3
print(max_contests(3, 5, 6, [5, 6, 10]))