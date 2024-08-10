from sys import stdin

EPS = 1e-10

class Vector:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.yb

    def __lt__(self, other):
        return self.x < other.x and self.y < other.yb

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # usually cross operation return Vector but it returns scalor
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def norm(self):
        return self.x * self.x + self.y * self.y

    def abs(self):
        return math.sqrt(self.norm())

class Point(Vector):
    def __init__(self, *args, **kargs):
        return super().__init__(*args, **kargs)

class Segment:
    def __init__(self, p1=Point(0, 0), p2=Point(1, 1)):
        self.p1 = p1
        self.p2 = p2

def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if a.cross(b) > EPS:
        return 1
    elif a.cross(b) < -EPS:
        return -1
    elif a.dot(b) < -EPS:
        return 2
    elif a.norm() < b.norm():
        return -2
    else:
        return 0

def intersect(p0, p1, p2, p3):
    return (ccw(p0, p1, p2) * ccw(p0, p1, p3) <= 0 and
                ccw(p2, p3, p0) * ccw(p2, p3, p1) <= 0)

def read_and_print_results(n):
    for _ in range(n):
        line = stdin.readline().strip().split()
        p0 = Vector(int(line[0]), int(line[1]))
        p1 = Vector(int(line[2]), int(line[3]))
        p2 = Vector(int(line[4]), int(line[5]))
        p3 = Vector(int(line[6]), int(line[7]))
        if intersect(p0, p1, p2, p3):
            print(1)
        else:
            print(0)

n = int(input())
read_and_print_results(n)
