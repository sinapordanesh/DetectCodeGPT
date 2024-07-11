class Node():
    def __init__(self, id, key):
        self.id = id
        self.key = key

    def setKeys(self, data):
        length = len(data)
        if ( self.id // 2 ) != 0:
            self.pk = data[self.id // 2]
        else :
            self.pk = -1
        if self.id * 2 < length:
             self.lk = data[self.id * 2]
        else :
            self.lk = -1
        if self.id * 2 + 1 < length:
             self.rk = data[self.id * 2 + 1]
        else :
            self.rk = -1

    def printInfo(self):
        print( "node " + str(self.id) + ": key = " + str(self.key), end=", " )
        if self.pk != -1:
            print( "parent key = " + str(self.pk), end = ", ")
        if self.lk != -1:
            print( "left key = " + str(self.lk), end = ", ")
        if self.rk != -1:
            print( "right key = " + str(self.rk) , end=", ")
        print()

def main():
    n = int( input() )
    inputs = input().split()
    for tmp in inputs:
        tmp = int(tmp)
    data = [0]
    data.extend(inputs)
    Tree = []
    for i in range(1, n+1):
        Tree.append( Node(i, data[i]) )
    for node in Tree:
        node.setKeys( data )
        node.printInfo()

if __name__ == '__main__':
    main()

