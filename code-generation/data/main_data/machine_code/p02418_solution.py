def find_pattern(s, p):
    if p in s + s:
        print("Yes")
    else:
        print("No")

s = input()
p = input()
find_pattern(s, p)