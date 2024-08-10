import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
#from collections import defaultdict
def main():
    n = int(input())
    s = tuple(map(int, tuple(input())))
    num_pos = [] # 各数字がｓ中に最後にあらわれる位置。
    for num in range(10):
        if num in s:
            num_pos.append(n - s[::-1].index(num) - 1)
    unique_num = [0] * n # ｓの各桁でその桁以降にある数字の種類。
    for i1 in range(n):
        unique_num[i1] = sum([np >= i1 for np in num_pos])
    unique_num.append(0)
    r = 0
    for keta1 in range(10):
        if keta1 in s:
            keta1_pos = s.index(keta1)
            for keta2 in range(10):
                if keta2 in s[keta1_pos + 1:]:
                    keta2_pos = s[keta1_pos + 1:].index(keta2) + keta1_pos + 1
                    r += unique_num[keta2_pos + 1]
    print(r)

if __name__ == '__main__':
    main()