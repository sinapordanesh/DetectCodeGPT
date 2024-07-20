def friends_who_can_ride(N, K, heights):
    count = 0
    for h in heights:
        if h >= K:
            count += 1
    return count

#Sample Input 1
print(friends_who_can_ride(4, 150, [150, 140, 100, 200]))

#Sample Input 2
print(friends_who_can_ride(1, 500, [499]))

#Sample Input 3
print(friends_who_can_ride(5, 1, [100, 200, 300, 400, 500]))