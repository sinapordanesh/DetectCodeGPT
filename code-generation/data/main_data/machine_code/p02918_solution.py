def max_happy_people(N, K, S):
    def count_happy_people(queue):
        count = 0
        for i in range(len(queue) - 1):
            if queue[i] == queue[i+1]:
                count += 1
        return count
    
    max_happy = count_happy_people(S)
    
    for l in range(1, K+1):
        for r in range(N):
            new_queue = S[:l] + S[l:r+1][::-1] + S[r+1:]
            max_happy = max(max_happy, count_happy_people(new_queue))
    
    return max_happy

# Sample Input 1
print(max_happy_people(6, 1, "LRLRRL"))

# Sample Input 2
print(max_happy_people(13, 3, "LRRLRLRRLRLLR"))

# Sample Input 3
print(max_happy_people(10, 1, "LLLLLRRRRR"))

# Sample Input 4
print(max_happy_people(9, 2, "RRRLRLRLL"))