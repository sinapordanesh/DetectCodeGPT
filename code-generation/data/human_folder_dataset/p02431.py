
from collections import UserList


class Vector(UserList):
    def push_back(self, v):
        self.data.append(v)

    def pop_back(self):
        return self.data.pop()


def run():
    vec = Vector()
    count = int(input())

    for i in range(count):
        com, *val = [int(x) for x in input().split()]
        if com == 0:
            vec.push_back(val[0])
        elif com == 1:
            print(vec[val[0]])
        elif com == 2:
            vec.pop_back()
        else:
            ValueError('invalid command')


if __name__ == '__main__':
    run()

