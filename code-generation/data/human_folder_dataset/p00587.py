import sys


def searchcenter (str):
    temp_layer = 0
    for x in range(len(str)):
        c = str[x]
        if c == '(':
            temp_layer += 1
        elif c == ')':
            temp_layer -= 1
        elif temp_layer == 1:
            return x

#whether either tree have common factor
def either_tree_have (t1len, t2len, center1_u, center2_u):
    if center1_u == 1 and center2_u == 1:
        return "right"
    elif center1_u == t1len -2 and center2_u == t2len -2:
        return "left"
    elif 4 <= center1_u and 4 <= center2_u and center1_u <= t1len - 5 and center2_u <= t2len - 5:
        return "both"
    elif center1_u == 1 and center2_u == t2len - 2:
        return "t1_rightandt2_left"
    elif center1_u == t1len - 2 and center2_u == 1:
        return "t1_leftandt2_right"
    elif center1_u == 1 and 4 <= center2_u and center2_u <= t2len - 5:
        return "t1_rightandt2_both"
    elif center1_u == t1len - 2 and 4 <= center2_u and center2_u <= t2len - 5:
        return "t1_leftandt2_both"
    elif 4 <= center1_u and center1_u <= t1len - 5 and center2_u == 1:
        return "t1_bothandt2_right"
    elif 4 <= center1_u and center1_u <= t1len - 5 and center2_u == t2len - 2:
        return "t1_bothandt2_left"
    else:
        return "no"

def operate_u (tree1, tree2):
    length_tree1 = len(tree1)
    length_tree2 = len(tree2)

    if length_tree1 == 3 or length_tree2 == 3:
        if length_tree1 != 3:
            tree2 = tree1
            length_tree2 = length_tree1
        elif length_tree2 != 3:
            tree1 = tree2
            length_tree1 = length_tree2
        else:
            return "(,)"


    center1_uo = searchcenter(tree1)
    center2_uo = searchcenter(tree2)

    e_result = either_tree_have(length_tree1, length_tree2, center1_uo, center2_uo)

    if e_result == "both":
        return "(" + operate_u(tree1[1:center1_uo], tree2[1:center2_uo]) + "," + operate_u(tree1[center1_uo + 1:-1], tree2[center2_uo + 1:-1]) + ")"
    elif e_result == "left":
        return "(" + operate_u(tree1[1:-2], tree2[1:-2]) + ",)"
    elif e_result == "right":
        return "(," + operate_u(tree1[2:-1], tree2[2:-1]) + ")"
    elif e_result == "t1_leftandt2_right":
        return "(" + operate_u(tree1[1:center1_uo], tree1[1:center1_uo]) + "," + operate_u(tree2[center2_uo + 1:-1], tree2[center2_uo + 1:-1]) + ")"
    elif e_result == "t1_rightandt2_left":
        return "(" + operate_u(tree2[1:center2_uo], tree2[1:center2_uo]) + "," + operate_u(tree1[center1_uo + 1:-1], tree1[center1_uo + 1:-1]) + ")"
    elif e_result == "t1_leftandt2_both":
        return "(" + operate_u(tree1[1:-2], tree2[1:center2_uo]) + "," + operate_u(tree2[center2_uo + 1:-1], tree2[center2_uo + 1:-1]) + ")"
    elif e_result == "t1_rightandt2_both":
        return "(" + operate_u(tree2[1:center2_uo], tree2[1:center2_uo]) + "," + operate_u(tree1[2:-1], tree2[center2_uo + 1:-1]) + ")"
    elif e_result == "t1_bothandt2_left":
        return "(" + operate_u(tree1[1:center1_uo], tree2[1:-2]) + "," + operate_u(tree1[center1_uo + 1:-1], tree1[center1_uo + 1:-1]) + ")"
    elif e_result == "t1_bothandt2_right":
        return "(" + operate_u(tree1[1:center1_uo], tree1[1:center1_uo]) + "," + operate_u(tree1[center1_uo + 1:-1], tree2[2:-1]) + ")"
    else:
        return "(,)"

#whether both tree have common factor
def both_tree_have (t1len, t2len, center1_i, center2_i):
    if 4 <= center1_i and 4 <= center2_i and center1_i <= t1len - 5 and center2_i <= t2len - 5:
        return "both"
    elif (center1_i == 1 and center2_i == t2len - 2) or (center1_i == t1len - 2 and center2_i == 1):
        return "no"
    elif center1_i == t1len - 2 or center2_i == t2len - 2:
        return "left"
    elif center1_i == 1 or center2_i == 1:
        return "right"
    else:
        return "no"


def operate_i (tree1, tree2):
    length_tree1 = len(tree1)
    length_tree2 = len(tree2)

    if length_tree1 == 3 or length_tree2 == 3:
        return "(,)"

    center1_io = searchcenter(tree1)
    center2_io = searchcenter(tree2)

    b_result = both_tree_have(length_tree1, length_tree2, center1_io, center2_io)

    if b_result == "both":
        return "(" + operate_i(tree1[1:center1_io], tree2[1:center2_io]) + "," + operate_i(tree1[center1_io + 1:-1], tree2[center2_io + 1:-1]) + ")"
    elif b_result == "left":
        return "(" + operate_i(tree1[1:center1_io], tree2[1:center2_io]) + ",)"
    elif b_result == "right":
        return "(," + operate_i(tree1[center1_io + 1:-1], tree2[center2_io + 1:-1]) + ")"
    else:
        return "(,)"

class Process:
    """superclass for polymofism"""
    def process(self):
        pass

class Intersection(Process):
    """i"""
    def __init__(self, tree1, tree2):
        self.tree1 = tree1
        self.tree2 = tree2
    def process(self):
        return operate_i(self.tree1, self.tree2)

class Unit(Process):
    """u"""
    def __init__(self, tree1, tree2):
        self.tree1 = tree1
        self.tree2 = tree2
    def process(self):
        return operate_u(self.tree1, self.tree2)

class BuilderProcess:
    """builder class"""
    def __init__(self, line):
        factor = line.split(" ")
        self.tree1 = factor[1]
        self.tree2 = factor[2][:-1]
        if factor[0] == 'i':
            self.task = Intersection(self.tree1, self.tree2)
        else:
            self.task = Unit(self.tree1, self.tree2)



if __name__ == '__main__':
    inputs = []
    for line in sys.stdin:
        inputs.append(line)

    for line in inputs:
        b = BuilderProcess(line)
        print(b.task.process())