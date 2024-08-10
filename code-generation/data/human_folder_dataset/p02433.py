class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def run():
    n = int(input())
    tail = Node(None)
    node = tail

    for _ in range(n):
        command = input()
        if command.startswith('0'):
            nn = Node(int(command[2:]))
            nn.prev, nn.next = node.prev, node
            if node.prev is not None:
                node.prev.next = nn
            node.prev = nn
            node = node.prev
        elif command.startswith('1'):
            i = int(command[2:])
            if i > 0:
                for _ in range(i):
                    node = node.next
            else:
                for _ in range(-i):
                    node = node.prev
        elif command.startswith('2'):
            p, n = node.prev, node.next
            node.prev, node.next = None, None
            node = n
            if p is None:
                n.prev = None
            else:
                n.prev, p.next = p, n
        else:
            raise ValueError('invalid command')

    st = []
    node = tail.prev
    while node is not None:
        st.append(node.value)
        node = node.prev

    while len(st) > 0:
        print(st.pop())


if __name__ == '__main__':
    run()
