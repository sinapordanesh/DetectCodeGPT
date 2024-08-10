def max_participants(N, participants):
    participants.sort(reverse=True)
    count = 0
    stack = []
    
    for i in range(N):
        if participants[i][0] >= len(stack) + 1:
            stack.append(participants[i][1])
            count += 1
    
    return count

# Sample Input 1
print(max_participants(3, [(0, 2), (1, 3), (3, 4)]))

# Sample Input 2
print(max_participants(3, [(2, 4), (3, 1), (4, 1)]))

# Sample Input 3
print(max_participants(10, [(1, 3), (8, 4), (8, 3), (9, 1), (6, 4), (2, 3), (4, 2), (9, 2), (8, 3), (0, 1)]))