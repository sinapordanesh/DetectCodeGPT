def double_linked_list(n, commands):
    class Node:
        def __init__(self, key):
            self.key = key
            self.prev = None
            self.next = None

    head = Node(None)
    tail = Node(None)
    head.next = tail
    tail.prev = head

    def insert(x):
        new_node = Node(x)
        new_node.next = head.next
        new_node.prev = head
        head.next.prev = new_node
        head.next = new_node

    def delete(x):
        current = head.next
        while current != tail:
            if current.key == x:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

    def deleteFirst():
        if head.next != tail:
            head.next.next.prev = head
            head.next = head.next.next

    def deleteLast():
        if head.next != tail:
            tail.prev.prev.next = tail
            tail.prev = tail.prev.prev

    for command in commands:
        if "insert" in command:
            insert(int(command.split()[1]))
        elif "delete" in command:
            delete(int(command.split()[1]))
        elif "deleteFirst" in command:
            deleteFirst()
        elif "deleteLast" in command:
            deleteLast()

    result = []
    current = head.next
    while current != tail:
        result.append(str(current.key))
        current = current.next

    return " ".join(result)

# Sample Input 1
n = 7
commands = ["insert 5", "insert 2", "insert 3", "insert 1", "delete 3", "insert 6", "delete 5"]
print(double_linked_list(n, commands))

# Sample Input 2
n = 9
commands = ["insert 5", "insert 2", "insert 3", "insert 1", "delete 3", "insert 6", "delete 5", "deleteFirst", "deleteLast"]
print(double_linked_list(n, commands))