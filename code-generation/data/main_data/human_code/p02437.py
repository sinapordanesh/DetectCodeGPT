

class MaxPQ:
    def __init__(self):
        self.q = []

    def insert(self, x):
        self.q.append(x)
        self.swim(len(self.q)-1)

    def get_max(self):
        if len(self.q) > 0:
            return self.q[0]
        else:
            return None

    def delete_max(self):
        if len(self.q) == 0:
            return

        val = self.q.pop()
        if len(self.q) > 0:
            self.q[0] = val
            self.sink(0)

    def sink(self, i):
        c1 = (i + 1) * 2 - 1
        c2 = (i + 1) * 2
        size = len(self.q)
        if c1 >= size:
            pass
        elif c1 < size and c2 >= size:
            if self.q[c1] > self.q[i]:
                self.q[c1], self.q[i] = self.q[i], self.q[c1]
                self.sink(c1)
        elif self.q[c1] > self.q[c2]:
            if self.q[c1] > self.q[i]:
                self.q[c1], self.q[i] = self.q[i], self.q[c1]
                self.sink(c1)
        else:
            if self.q[c2] > self.q[i]:
                self.q[c2], self.q[i] = self.q[i], self.q[c2]
                self.sink(c2)

    def swim(self, i):
        p = (i+1) // 2 - 1
        if p >= 0:
            if self.q[p] < self.q[i]:
                self.q[p], self.q[i] = self.q[i], self.q[p]
                self.swim(p)


def run():
    n, q = [int(x) for x in input().split()]
    pqs = [MaxPQ() for _ in range(n)]

    for _ in range(q):
        com = [int(x) for x in input().split()]
        c = com[0]
        if c == 0:
            t, v = com[1:]
            pqs[t].insert(v)
        elif c == 1:
            t = com[1]
            val = pqs[t].get_max()
            if val is not None:
                print(val)
        elif c == 2:
            t = com[1]
            pqs[t].delete_max()
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

