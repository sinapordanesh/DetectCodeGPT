def min_communication(N, A, B, C, members, M, friendships):
    grade_chat = {1:[], 2:[], 3:[]}
    for i in range(1, N+1):
        if i in members[0]:
            grade_chat[1].append(i)
        elif i in members[1]:
            grade_chat[2].append(i)
        else:
            grade_chat[3].append(i)
    
    min_communication = float('inf')
    best_student = -1
    
    for i in range(1, N+1):
        communication = set()
        for friend in friendships:
            if i == friend[0]:
                communication.add(friend[1])
            elif i == friend[1]:
                communication.add(friend[0])
        
        count_communication = len(communication)
        if count_communication < min_communication:
            if all(member in communication for member in grade_chat[1]) and all(member in communication for member in grade_chat[2]) and all(member in communication for member in grade_chat[3]):
                min_communication = count_communication
                best_student = i
    
    return min_communication, best_student

# Sample Input 1
N = 4
A = 2
B = 1
C = 1
members = [[1, 2], [3], [4]]
M = 3
friendships = [[1, 2], [2, 4], [3, 4]]

print(min_communication(N, A, B, C, members, M, friendships))

# Sample Input 2
N = 4
A = 1
B = 1
C = 1
members = [[2], [3], [4]]
M = 4
friendships = [[1, 2], [1, 3], [1, 4], [2, 4]]

print(min_communication(N, A, B, C, members, M, friendships))

# Sample Input 3
N = 8
A = 1
B = 2
C = 2
members = [[5], [4, 6], [3, 8]]
M = 7
friendships = [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [2, 6]]

print(min_communication(N, A, B, C, members, M, friendships))