def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "YES"
    else:
        return "NO"

N = int(input())
for _ in range(N):
    a, b, c = map(int, input().split())
    print(is_right_triangle(a, b, c))