class Node():
    def __init__(self):
        self.lt = None
        self.rt = None
        self.dep = None

class Trie():
    def __init__(self):
        self.root = Node()
        self.root.dep = 0

    def add(self, string):
        node = self.root
        for s in string:
            if s == '0':
                if node.lt is None:
                    node.lt = Node()
                    node.lt.dep = node.dep + 1
                node = node.lt
            else:
                if node.rt is None:
                    node.rt = Node()
                    node.rt.dep = node.dep + 1
                node = node.rt

N, L = map(int, input().split())

trie = Trie()

for _ in range(N):
    s = input()
    trie.add(s)

subgame = []
stack = [trie.root]

while stack:
    node = stack.pop()
    if node.lt is None and node.rt is None:
        continue
    elif node.rt is None:
        stack.append(node.lt)
        subgame.append(L - node.dep)
    elif node.lt is None:
        stack.append(node.rt)
        subgame.append(L - node.dep)
    else:
        stack.append(node.lt)
        stack.append(node.rt)

def grundy(n):
    if n == 0: return 0
    if n % 2 == 1: return 1
    if n == 2**(n.bit_length() - 1):
        return n
    return grundy(n - 2**(n.bit_length() - 1))

g = 0

for l in subgame:
    g ^= grundy(l)

print('Alice' if g != 0 else 'Bob')