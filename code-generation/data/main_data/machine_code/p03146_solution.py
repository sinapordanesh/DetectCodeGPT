def find_minimum_integer(s):
    a = [s]
    while True:
        if a[-1] % 2 == 0:
            a.append(a[-1] // 2)
        else:
            a.append(3 * a[-1] + 1)
        
        if a.count(a[-1]) > 1:
            return a.index(a[-1])

s = int(input())
print(find_minimum_integer(s))