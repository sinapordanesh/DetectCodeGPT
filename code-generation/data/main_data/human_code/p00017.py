import string
def cipher(s, i):
    if s in string.ascii_lowercase:
        return string.ascii_lowercase[(ord(s) - ord('a')+ i) % 26]
    elif s in string.ascii_uppercase:
        return string.ascii_uppercase[(ord(s) - ord('A')+ i) % 26]
    else:
        return s

def decode(s, i):
    return ''.join([cipher(x, i) for x in s])

while True:
    try:
        sent = input().split()
    except:
        break

    for i in range(26):
        si = [decode(s, i) for s in sent]
        if 'the' in si or 'this' in si or 'that' in si:
            print(' '.join(si))