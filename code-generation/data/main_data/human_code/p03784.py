A, B = map(int, input().split(" "))

if A <= B:
    print("Impossible")
    exit(0)

chain = []
N = A + B

def ask(i, j):
    print("? %d %d" % (i, j))
    return input() == 'Y'

for i in range(0, N):
    if len(chain) == 0:
        chain.append(i)
        continue
    last = chain[-1]
    if ask(last, i):
        chain.append(i)
    else:
        chain.pop()

main = chain.pop()
ret = [ ('1' if ask(main, x) else '0') for x in range(0, N) ]

print("! %s" % ("".join(ret)))
