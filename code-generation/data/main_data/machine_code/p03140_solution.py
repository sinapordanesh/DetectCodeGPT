def min_operations(n, a, b, c):
    operations = 0
    for i in range(n):
        if a[i] != b[i] and b[i] != c[i] and a[i] != c[i]:
            operations += 2
        elif a[i] != b[i] or b[i] != c[i] or a[i] != c[i]:
            operations += 1
    return operations

n = int(input())
a = input()
b = input()
c = input()

print(min_operations(n, a, b, c))