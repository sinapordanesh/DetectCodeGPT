def good_sequence(N, a):
    count = {}
    for num in a:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    remove = 0
    for num in count:
        if count[num] > num:
            remove += count[num] - num
            
    return remove

#Sample Input 1
print(good_sequence(4, [3, 3, 3, 3]))

#Sample Input 2
print(good_sequence(5, [2, 4, 1, 4, 2]))

#Sample Input 3
print(good_sequence(6, [1, 2, 2, 3, 3, 3]))

#Sample Input 4
print(good_sequence(1, [1000000000]))

#Sample Input 5
print(good_sequence(8, [2, 7, 1, 8, 2, 8, 1, 8]))