def ketawa(x):
    l = list(str(x))
    wa = 0
    for a in l:
        wa += int(a)
    return wa

n = int(input())
lst = list(str(n))
keta = len(str(n))




nine = int("".join([lst[0]] + ["9"]*(keta-1)))

if nine <= n:
    print(ketawa(nine))
else:
    lst_head = str(int(lst[0]) - 1)
    nine = int("".join([lst_head] + ["9"]*(keta-1)))
    print(ketawa(nine))