def postorder_tree_walk(preorder, inorder):
    if not preorder:
        return []
        
    root = preorder[0]
    root_index = inorder.index(root)
    
    left_preorder = preorder[1:root_index+1]
    left_inorder = inorder[:root_index]
    
    right_preorder = preorder[root_index+1:]
    right_inorder = inorder[root_index+1:]
    
    return postorder_tree_walk(left_preorder, left_inorder) + postorder_tree_walk(right_preorder, right_inorder) + [root]

n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

postorder = postorder_tree_walk(preorder, inorder)
print(' '.join(map(str, postorder)) )