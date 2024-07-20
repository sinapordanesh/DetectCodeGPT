def intersection_of_circles(c1x, c1y, c1r, c2x, c2y, c2r):
    distance = ((c1x - c2x)**2 + (c1y - c2y)**2)**0.5
    
    if distance > c1r + c2r:
        return 4
    elif distance == c1r + c2r:
        return 3
    elif distance < c1r + c2r and distance > abs(c1r - c2r):
        return 2
    elif distance == abs(c1r - c2r):
        return 1
    else:
        return 0

# Sample Input
print(intersection_of_circles(1, 1, 1, 6, 2, 2)) # Sample Output: 4
print(intersection_of_circles(1, 2, 1, 4, 2, 2)) # Sample Output: 3
print(intersection_of_circles(1, 2, 1, 3, 2, 2)) # Sample Output: 2
print(intersection_of_circles(0, 0, 1, 1, 0, 2)) # Sample Output: 1
print(intersection_of_circles(0, 0, 1, 0, 0, 2)) # Sample Output: 0