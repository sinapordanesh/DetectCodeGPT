
from collections import UserList


class LexicalOrderedList(UserList):
    def __eq__(self, other):
        len_a = len(self)
        len_b = len(other)
        if len_a != len_b:
            return False
        i = 0
        while self.data[i] == other.data[i]:
            i += 1

        return i == len_a

    def __gt__(self, other):
        len_a = len(self)
        len_b = len(other)

        i = 0
        while (i < len_a and i < len_b
               and self.data[i] == other.data[i]):
            i += 1

        if i == len_a and i == len_b:
            return False
        elif i == len_a and i < len_b:
            return False
        elif i < len_a and i == len_b:
            return True
        else:
            return self.data[i] > other.data[i]

    def __ge__(self, other):
        return self == other or self > other


def run():
    n = int(input())
    a = LexicalOrderedList()
    for c in input().split():
        a.append(int(c))
    assert len(a) == n

    m = int(input())
    b = LexicalOrderedList()
    for c in input().split():
        b.append(int(c))
    assert len(b) == m

    if b > a:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    run()

