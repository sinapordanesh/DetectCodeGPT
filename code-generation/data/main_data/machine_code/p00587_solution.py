def tree_intersection_union(operation, tree1, tree2):
    if operation == 'i':
        result = ""
        for i in range(len(tree1)):
            if tree1[i] == tree2[i]:
                result += tree1[i]
        return result
    elif operation == 'u':
        result = ""
        for i in range(len(tree1)):
            if tree1[i] != ',' and tree2[i] != ',':
                result += tree1[i]
            elif tree1[i] == ',':
                result += tree2[i]
            else:
                result += tree1[i]
        return result