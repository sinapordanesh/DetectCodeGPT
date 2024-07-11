
def reverseString(s):
        return s[::-1]


while True:
    try:
        s = str(input())
        s = reverseString(s)
        print(s)
    except:
        break
