def find_polynomial(p, a):
    for i in range(p):
        print((a[(i-1)%p] + a[i]) % p, end=" ")

# Sample Input
p = 5
a = [0, 1, 0, 1, 0]

find_polynomial(p, a)