def minimum_distance(W, a, b):
    if a <= b <= a+W or b <= a <= b+W:
        return 0
    else:
        return min(abs(a - (b + W)), abs(b - (a + W)))

# Taking input
inputs = input().split()
W = int(inputs[0])
a = int(inputs[1])
b = int(inputs[2])

print(minimum_distance(W, a, b))