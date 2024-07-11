class Dice(object):
 
    def __init__(self, d):

        self.rows = [d[0], d[4], d[5], d[1]]
        self.cols = [d[0], d[2], d[5], d[3]]
 
    def __move_next(self, x, y):
        temp = y.pop(0)
        y.append(temp)
        x[0] = y[0]
        x[2] = y[2]
 
    def __move_prev(self, x, y):
        temp = y.pop(3)
        y.insert(0, temp)
        x[0] = y[0]
        x[2] = y[2]
 
    def execute(self, c):
        for i in c:
            self.__move(i, self.rows, self.cols)
 
    def __move(self, com, x, y):
        if com == "N":
            self.__move_prev(y, x)
        elif com == "S":
            self.__move_next(y, x)
        elif com == "E":
            self.__move_prev(x, y)
        elif com == "W":
            self.__move_next(x, y)
 
    def print_top(self):
        print(self.rows[0])
    
    def execute2(self, a, b):
        self.__rot(a)
        if a == self.rows[0] or a == self.rows[2]:
            self.__move_prev(self.cols, self.rows)    
        
        self.__rot(b)
        
        while a != self.rows[0]:
            self.__move_prev(self.cols, self.rows)    
        
        if b == self.rows[1]:
            print(self.cols[3])
        elif b == self.rows[3]:
            print(self.cols[1])
        
    def __rot(self, z):
        i = 0
        while z not in self.rows:
            self.__move_next(self.rows, self.cols)
            if i > 3:
                self.__move_next(self.cols, self.rows)
                i = 0
            i+=1

d = list(map(int, input().split(" ")))
c = int(input()) 
dice = Dice(d)

for i in range(c):
    a, b = map(int, input().split(" "))
    dice.execute2(a,b)

