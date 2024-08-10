
def count_characters(word, dic, kcs, kcs2, kcs2_1):
    prev1 = None
    i = 0
    l = len(word)
    while i < l:
        c = word[i]
        if c in kcs2_1 and i < l - 1:
            c2 = word[i + 1]
            if (c + c2) in kcs2:
                if prev1 != None:
                    dic[prev1][c + c2] += 1
                prev1 = c + c2
                i += 2
                continue
        if prev1 != None:
            dic[prev1][c] += 1
        prev1 = c
        i += 1

kcs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
kcs2 = ["ld", "mb", "mp", "nc", "nd", "ng", "nt", "nw", "ps", "qu", "cw", "ts"]
kcs2_1 = ["l", "m", "n", "p", "q", "c", "t"]

n = int(input())
dic = {}
for c in (kcs + kcs2):
    table = {}
    for c1 in (kcs + kcs2):
        table[c1] = 0
    dic[c] = table

for i in range(n):
    words = input().split()
    for word in words:
        count_characters(word, dic, kcs, kcs2, kcs2_1)

for c in (kcs + kcs2):
    occurence_table = dic[c]
    max_c = "a"
    max_n = 0
    for k, v in occurence_table.items():
        if v > max_n:
            max_n = v
            max_c = k
    print(c, max_c, max_n)