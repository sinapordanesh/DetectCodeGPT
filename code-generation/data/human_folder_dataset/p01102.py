def testcase_ends():
    s = input()
    if s == '.':
        return True

    t = input()

    if s == t:
        print('IDENTICAL')
        return False

    s0 = s.split('"')[0::2]
    s1 = s.split('"')[1::2]
    t0 = t.split('"')[0::2]
    t1 = t.split('"')[1::2]

    if s0 != t0:
        print('DIFFERENT')
        return False

    if len(s1) != len(t1):
        print('DIFFERENT')
        return False

    if len([(ss, tt) for ss, tt in zip(s1, t1) if ss != tt]) == 1:
        print('CLOSE')
    else:
        print('DIFFERENT')

    return False

def main():
    while not testcase_ends():
        pass

main()

