def min_additional_chairs(N, M, LR):
    LR.sort(key=lambda x: (x[1], -x[0]))
    chairs = [0]
    
    for l, r in LR:
        chairs.append(l)
        chairs.append(r+1)
    
    chairs.sort()
    ans = 0
    for i in range(1, len(chairs)):
        ans = max(ans, chairs[i]-chairs[i-1])
    
    return ans - 1

# Sample Input 1
print(min_additional_chairs(4, 4, [[0, 3], [2, 3], [1, 3], [3, 4]]))

# Sample Input 2
print(min_additional_chairs(7, 6, [[0, 7], [1, 5], [3, 6], [2, 7], [1, 6], [2, 6], [3, 7]]))

# Sample Input 3
print(min_additional_chairs(3, 1, [[1, 2], [1, 2], [1, 2]]))

# Sample Input 4
print(min_additional_chairs(6, 6, [[1, 6], [1, 6], [1, 5], [1, 5], [2, 6], [2, 6]]))