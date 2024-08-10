masks = []
for _ in range(int(input())):
    k, *b = map(int, input().split())
    mask = 0
    for i in range(k):
        mask += 1 << b[i]
    masks.append(mask)
x = 0
MASK = (1<<64) - 1
def test(i):
    global x
    print(+((x & (1 << i)) > 0))
def Set(i):
    global x
    global masks
    x |= masks[i]
def clear(i):
    global x
    global masks
    x = (x | masks[i]) ^ masks[i]
def flip(i):
    global x
    global masks
    x ^= masks[i]
def all(i):
    global x
    global masks
    print(+(x & masks[i] == masks[i]))
def any(i):
    global x
    global masks
    print(+(x & masks[i] > 0))
def none(i):
    global x
    global masks
    print(+(x & masks[i] == 0))
def count(i):
    global x
    global masks
    print(bin(x & masks[i]).count('1'))
def val(i):
    global x
    global masks
    print(x & masks[i])
    
f = [test, Set, clear, flip, all, any, none, count, val].__getitem__
for _ in range(int(input())):
    op, *i = map(int, input().split())
    f(op)(*i)
