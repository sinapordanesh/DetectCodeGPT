def calcAreas(sections):
    areas = []

    for s in sections:
        if len(s) <= 1:
            continue;

        areas.append(toArea(s))

    return areas

def toArea(section):
    a = 0
    b, _ = section[0]

    for s, e in section:
        a += (max(s, e) - b) - (0.5 if s != e else 0)

    return int(a)

def toDelta(p):
    if '/' == p:
        return -1
    if '\\' == p:
        return 1
    return 0

def toPaths(path):
    h = 0
    ph = 0
    paths = []

    for p in path:
        h += toDelta(p)
        paths.append((ph,h))
        ph = h

    return paths

def update(sections):
    [(lf, ll)] = sections.pop()

    n = None

    for i in range(len(sections)-1, -1, -1):
        if sections[i][0][0] == ll:
            n = i
            break

    if n == None:
        sections.append([(lf, ll)])
        return False

    lst = [(lf, ll)]
    for i in range(len(sections)-1, n-1, -1):
        s = sections.pop()
        lst = s + lst

    sections.append(lst)
    return True

def main():
    paths = toPaths(input())

    prev = -1
    sections = []

    prev_update = True

    for f, l in paths:
        sections.append([(f, l)])
        if l < prev:
            if prev_update:
                prev_update = update(sections)
        else:
            prev_update = True

        prev = l

    areas = calcAreas(sections)
    l = len(areas)

    print(sum(areas))
    print(l, end='')
    if l > 0:
        print(' {}'.format(' '.join([str(x) for x in areas])), end='')
    print()

if __name__ == '__main__':
    main()

