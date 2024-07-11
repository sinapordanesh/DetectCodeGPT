x = 0
mask = 2**64 - 1
def test(i):
    global x
    print(+((x & (1 << i)) != 0))
def Set(i):
    global x
    x |= 1 << i
def clear(i):
    global x
    x &= mask - (1 << i)
def flip(i):
    global x
    x ^= 1 << i
def all():
    global x
    print(+(x == mask))
def any():
    global x
    print(+(x != 0))
def none():
    global x
    print(+(x == 0))
def count():
    global x
    print(bin(x).count('1'))
def val():
    global x
    print(x)
    
f = [test, Set, clear, flip, all, any, none, count, val].__getitem__
for _ in range(int(input())):
    op, *i = map(int, input().split())
    f(op)(*i)
