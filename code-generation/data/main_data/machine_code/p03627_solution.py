def max_rectangle_area(N, sticks):
    sticks.sort(reverse=True)
    for i in range(N-3):
        if sticks[i] == sticks[i+1]:
            return sticks[i] * sticks[i+2]
    return 0

#Sample Input 1
print(max_rectangle_area(6, [3, 1, 2, 4, 2, 1]))

#Sample Input 2
print(max_rectangle_area(4, [1, 2, 3, 4]))

#Sample Input 3
print(max_rectangle_area(10, [3, 3, 3, 3, 4, 4, 4, 5, 5, 5]))