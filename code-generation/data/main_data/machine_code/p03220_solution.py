def build_palace(N, T, A, *H):
    closest_temp = float('inf')
    palace_index = -1
    for i in range(N):
        temp = T - H[i]*0.006
        if abs(temp - A) < closest_temp:
            closest_temp = abs(temp - A)
            palace_index = i + 1
    return palace_index

#Sample Input 1
print(build_palace(2, 12, 5, 1000, 2000))

#Sample Input 2
print(build_palace(3, 21, -11, 81234, 94124, 52141))