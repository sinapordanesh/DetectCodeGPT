def tree_walk(n, nodes):
    def preorder(node):
        if node == -1:
            return []
        return [node] + preorder(nodes[node][0]) + preorder(nodes[node][1])
    
    def inorder(node):
        if node == -1:
            return []
        return inorder(nodes[node][0]) + [node] + inorder(nodes[node][1])
    
    def postorder(node):
        if node == -1:
            return []
        return postorder(nodes[node][0]) + postorder(nodes[node][1]) + [node]
    
    nodes = [list(map(int, nodes[i].split())) for i in range(n)]
    
    print("Preorder")
    print(" ".join([" " + str(x) for x in preorder(0)]))
    
    print("Inorder")
    print(" ".join([" " + str(x) for x in inorder(0)]))
    
    print("Postorder")
    print(" ".join([" " + str(x) for x in postorder(0)])).__assistant__()
    
# Sample input
n = 9
nodes = ["0 1 4", "1 2 3", "2 -1 -1", "3 -1 -1", "4 5 8", "5 6 7", "6 -1 -1", "7 -1 -1", "8 -1 -1"]

tree_walk(n, nodes)