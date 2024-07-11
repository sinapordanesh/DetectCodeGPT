N = int(input())

class Node():
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right

T = [Node() for _ in range(N)]

for _ in range(N):
    id, left, right = map(int, input().split())

    T[id].left = left
    T[id].right = right

    if left != -1:
        T[left].parent = id
    if right != -1:
        T[right].parent = id


def preorder(id):
    preorder_list.append(id)

    if T[id].left != -1:
        preorder(T[id].left)
    if T[id].right != -1:
        preorder(T[id].right)

def inorder(id):
    left = T[id].left
    right = T[id].right

    if left != -1:
        inorder(T[id].left)
    inorder_list.append(id)

    if right != -1:
        inorder(right)

def get_right_sibling(id):
    parent_id = T[id].parent
    if parent_id == -1:
        return -1
    if T[parent_id].right != id:
        return T[parent_id].right

    return -1

def postorder(id):
    left = T[id].left
    right = T[id].right

    if left != -1:
        postorder(left)

    if right != -1:
        postorder(right)

    postorder_list.append(id)

preorder_list = []
inorder_list = []
postorder_list = []
for id in range(N):
    if T[id].parent == -1:
        preorder(id)
        inorder(id)
        postorder(id)
        break


print("Preorder")
print(" "+" ".join(map(str, preorder_list)))
print("Inorder")
print(" "+" ".join(map(str, inorder_list)))
print("Postorder")
print(" "+" ".join(map(str, postorder_list)))
