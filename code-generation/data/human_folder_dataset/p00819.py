def decodeJ(s):
    return s[-1] + s[:-1]
def decodeC(s):
    return s[1:] + s[0]
def decodeE(s):
    lenS = len(s)
    return s[lenS//2:] + s[:lenS//2] if lenS % 2 == 0 else s[lenS//2+1:] + s[lenS//2] + s[:lenS//2]
def decodeA(s):
    return s[::-1]
def decodeP(s):
    ret = []
    for i in s:
        try:
            ret.append(str((int(i)-1)%10))
        except:
            ret.append(i)
    return ''.join(ret)
def decodeM(s):
    ret = []
    for i in s:
        try:
            ret.append(str((int(i)+1)%10))
        except:
            ret.append(i)
    return ''.join(ret)

N = int(input())
decode = {'J': decodeJ, 'C': decodeC, 'E': decodeE, 'A': decodeA, 'P': decodeP, 'M': decodeM}
for _ in range(N):
    messengers = input()
    message = input()
    for m in messengers[::-1]:
        message = decode[m](message)
    print(message)