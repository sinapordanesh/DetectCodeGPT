import math

def roundup1000(num):
    return math.ceil(num  / 1000) * 1000

debt = 100000
for _ in range(int(input())):
    debt = roundup1000(debt * 1.05)
print(debt)