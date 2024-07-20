import re

num = re.compile(r'\d+$')

def testcase_ends():
    n = int(input())
    if n == 0:
        return 1

    marks = [input().replace('-', '') for i in range(n)]
    links = {}
    bares = []
    labels = {}
    for i, mark in enumerate(marks, 1):
        if not mark:
            bares.append(i)
            continue

        v = False
        if mark.endswith('v'):
            mark = mark[:-1]
            links[i+1] = i
            v = True

        m = num.search(mark)
        if m is None:
            continue

        m = int(m.group())
        mark = num.sub('', mark)

        if m == 1:
            if mark in labels:
                links[i] = labels[mark]
                del labels[mark]
            if not v:
                bares.append(i)
        else:
            if mark in labels:
                links[i] = labels[mark]

            labels[mark] = i

    for w in bares:
        print(w)
        while w in links:
            w = links[w]
            print(w)

    return 0

def main():
    while not testcase_ends():
        pass

if __name__ == '__main__':
    main()

