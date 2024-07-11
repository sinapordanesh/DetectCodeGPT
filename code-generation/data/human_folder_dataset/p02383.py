class Daise:
    def __init__(self, info_list):
        self.T = info_list[0]
        self.S = info_list[1]
        self.E = info_list[2]
        self.W = info_list[3]
        self.N = info_list[4]
        self.B = info_list[5]
    
    def change(self, axis):
        if axis == 'S':
            self.T, self.B, self.S, self.N = self.N, self.S, self.T, self.B
        
        elif axis == 'E':
            self.T, self.B, self.E, self.W = self.W, self.E, self.T, self.B
        
        elif axis == 'W':
            self.T, self.B, self.W, self.E = self.E, self.W, self.T, self.B
        
        elif axis == 'N':
            self.T, self.B, self.N, self.S = self.S, self.N, self.T, self.B


if __name__ == '__main__':
    info = list(map(str, input().split()))
    axis = str(input())
    obj = Daise(info)

    for i in axis:
        obj.change(i)
    print(obj.T)
