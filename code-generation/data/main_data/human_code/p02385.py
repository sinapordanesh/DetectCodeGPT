class Dice(object):
 
    def __init__(self, d):

        self.rows = [d[0], d[4], d[5], d[1]]
        self.cols = [d[0], d[2], d[5], d[3]]
 
    def move_next_rows(self):
        temp = self.rows.pop(0)
        self.rows.append(temp)
        self.__update(self.cols, self.rows)

    def move_prev_rows(self):
        temp = self.rows.pop(3)
        self.rows.insert(0, temp)
        self.__update(self.cols, self.rows)
    
    def move_next_cols(self):
        temp = self.cols.pop(0)
        self.cols.append(temp)
        self.__update(self.rows, self.cols)
 
    def move_prev_cols(self):
        temp = self.cols.pop(3)
        self.cols.insert(0, temp)
        self.__update(self.rows, self.cols)

    def __update(self, x, y):
        x[0] = y[0]
        x[2] = y[2]
 
class DiceChecker(object):

    def __init__(self, dice1, dice2):
        self.dice1 = dice1
        self.dice2 = dice2
        self.dice1_top = self.dice1.rows[0]
        self.dice1_front = self.dice1.rows[3]
        
    def check_same_dice(self):

        is_same = False
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    is_same_element = self.dice1.rows == self.dice2.rows and self.dice1.cols == self.dice2.cols
                    if is_same_element: 
                        is_same = True
                    self.__rot(self.dice2)
                self.dice2.move_next_rows()
            self.dice2.move_next_cols()
            
        if is_same:
            print("Yes")
        else:
            print("No")
    
    def __rot(self, dice):
        temp = dice.rows[1]
        dice.rows[1] = dice.cols[3]
        dice.cols[3] = dice.rows[3]
        dice.rows[3] = dice.cols[1]
        dice.cols[1] = temp

        
d1 = list(map(int, input().split(" ")))
d2 = list(map(int, input().split(" ")))
dice1 = Dice(d1)
dice2 = Dice(d2)

dice_checker = DiceChecker(dice1, dice2)
dice_checker.check_same_dice()

