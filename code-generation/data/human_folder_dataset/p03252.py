import sys
from collections import Counter


def main():
    s = input()
    t = input()
    s_count = [0]*26
    t_count = [0]*26
    for i in range(ord("a"), ord("z")+1):
        s_count[i-97] = s.count(chr(i))
        t_count[i-97] = t.count(chr(i))
    s_count.sort()
    t_count.sort()
    if s_count == t_count:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
