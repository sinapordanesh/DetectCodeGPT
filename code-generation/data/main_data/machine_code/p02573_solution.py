def min_groups(N, M, friendships):
    friends = {}
    for i in range(1, N+1):
        friends[i] = set()
    
    for A, B in friendships:
        friends[A].add(B)
        friends[B].add(A)
    
    groups = 0
    visited = set()
    
    def dfs(person):
        visited.add(person)
        for friend in friends[person]:
            if friend not in visited:
                dfs(friend)
    
    for person in range(1, N+1):
        if person not in visited:
            groups += 1
            dfs(person)
    
    return groups

# Sample Input 1
print(min_groups(5, 3, [(1,2), (3,4), (5,1)]))

# Sample Input 2
print(min_groups(4, 10, [(1,2), (2,1), (1,2), (2,1), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]))

# Sample Input 3
print(min_groups(10, 4, [(3,1), (4,1), (5,9), (2,6)]))