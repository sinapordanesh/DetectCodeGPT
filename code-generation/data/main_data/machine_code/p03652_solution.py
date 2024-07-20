def min_participants(N, M, sports):
    max_participants = 0
    for i in range(1, M+1):
        participants = sum([1 for j in range(N) if i in sports[j]])
        max_participants = max(max_participants, participants)
    return max_participants

#Sample Input 1
print(min_participants(4, 5, [[5, 1, 3, 4, 2], [2, 5, 3, 1, 4], [2, 3, 1, 4, 5], [2, 5, 4, 3, 1]]))

#Sample Input 2
print(min_participants(3, 3, [[2, 1, 3], [2, 1, 3], [2, 1, 3]]))