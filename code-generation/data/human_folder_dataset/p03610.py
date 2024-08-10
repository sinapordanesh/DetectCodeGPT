s = input()
even = []

def listtostring(some):
    str1 = ""

    for ele in some:
        str1 += ele

    print(str1)

for i in range(len(s)):
    moji = s[i]
    if i % 2 == 0:
        even.append(moji)

listtostring(even)