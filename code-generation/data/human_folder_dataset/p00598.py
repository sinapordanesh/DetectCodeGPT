import sys

def rpn(str):
    r = []
    stack = []
    for i in range(0, len(str)):
        c = str[i]
        if c in "idsu":
            while len(stack) > 0:
                if stack[-1] in "idsuc":
                    a = stack.pop()
                    r.extend(a)
                else:
                    break
            stack.extend(c)
        elif c == "c":
            stack.extend(c)
        elif c == "(":
            stack.extend(c)
        elif c == ")":
            while len(stack) > 0:
                a = stack.pop()
                if a == "(":
                    break
                r.extend(a)
        else:
            r.extend(c)
    while len(stack) > 0:
        a = stack.pop()
        r.extend(a)
    return r

def intersect(a, b):
    r = []
    for e in a:
        if e in b:
            r.extend([e])
    return r

def union(a, b):
    r = list(set(a + b))
    return r

def diff(a, b):
    r = []
    for e in a:
        if e not in b:
            r.extend([e])
    return r

def universal(sets):
    r = []
    for v in sets.values():
        r.extend(v)
    r = list(set(r))
    return r

def calc(rpn, sets):
    stack = []
    U = universal(sets)
    for c in rpn:
        if c in "iuds":
            op2 = stack.pop()
            op1 = stack.pop()
            if c == "i":
                x = intersect(op1, op2)
                stack.append(x)
            elif c == "u":
                x = union(op1, op2)
                stack.append(x)
            elif c == "d":
                x = diff(op1, op2)
                stack.append(x)
            elif c == "s":
                x = diff(op1, op2)
                y = diff(op2, op1)
                z = union(x, y)
                stack.append(z)
        elif c == "c":
            op1 = stack.pop()
            x = diff(U, op1)
            stack.append(x)
        else:
            stack.append(sets[c])
    return stack.pop()
            
lno = 0
sets = {}
name = ""
for line in sys.stdin:
    lno += 1
    if lno % 2 == 1:
        name = line.strip().split()[0]
    elif name != "R":
        elem = list(map(int, line.strip().split()))
        sets[name] = elem
    else:
        e = rpn(line.strip())
        result = calc(e, sets)
        result.sort()
        if len(result) > 0:
            print(" ".join([str(n) for n in result]))
        else:
            print("NULL")
        sets = {}
