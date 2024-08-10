def max_honest_persons(N, testimonies):
    def check_honest(person, honest_set):
        for i in range(len(testimonies[person])):
            if testimonies[person][i][1] == 1 and testimonies[person][i][0] not in honest_set:
                return False
            if testimonies[person][i][1] == 0 and testimonies[person][i][0] in honest_set:
                return False
        return True

    def backtrack(person, honest_set):
        if person == N:
            return len(honest_set)
        
        count1, count2 = 0, 0
        
        if check_honest(person, honest_set.union({person+1})):
            count1 = backtrack(person+1, honest_set.union({person+1}))
        
        count2 = backtrack(person+1, honest_set)
        
        return max(count1, count2)
    
    testimonies_dict = {}
    for i in range(N):
        A = testimonies[i][0]
        testimonies_dict[i+1] = []
        for j in range(A):
            testimonies_dict[i+1].append((testimonies[i][2*j+1], testimonies[i][2*j+2]))
    
    return backtrack(0, set())

# Sample Input 1
print(max_honest_persons(3, [1, 2, 1, 1, 1, 1, 2, 0])) 

# Sample Input 2
print(max_honest_persons(3, [2, 2, 3, 0, 2, 3, 1, 0, 2, 1, 2, 0]))

# Sample Input 3
print(max_honest_persons(2, [1, 2, 0, 1, 1, 0]))