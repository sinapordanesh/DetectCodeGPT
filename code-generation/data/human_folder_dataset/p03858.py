import bisect
import sys
from collections import defaultdict


class RandomizedBinarySearchTree:
    def __init__(self):
        self.children = [[-1], [-1]]
        self.values = [0]
        self.counts = [0]
        self.root = 0

    def merge(self, left_root, right_root):
        children = self.children
        counts = self.counts
        li = left_root
        ri = right_root
        stack = []
        switch = 0
        while li != 0 and ri != 0:
            if switch:
                stack.append((li, 1))
                li = children[1][li]
            else:
                stack.append((ri, 0))
                ri = children[0][ri]
            switch ^= 1

        i = li if li != 0 else ri
        while stack:
            pi, is_right = stack.pop()
            children[is_right][pi] = i
            counts[pi] = counts[children[0][pi]] + counts[children[1][pi]] + 1
            i = pi

        return i

    def split(self, root, x):
        i = root
        lefts, rights = self.children
        values = self.values
        counts = self.counts
        l_stack = []
        r_stack = []
        while i != 0:
            if x < values[i]:
                r_stack.append(i)
                i = lefts[i]
            else:
                l_stack.append(i)
                i = rights[i]

        li, ri = 0, 0
        while l_stack:
            pi = l_stack.pop()
            rights[pi] = li
            counts[pi] = counts[lefts[pi]] + counts[li] + 1
            li = pi
        while r_stack:
            pi = r_stack.pop()
            lefts[pi] = ri
            counts[pi] = counts[ri] + counts[rights[pi]] + 1
            ri = pi

        return li, ri

    def insert(self, x):
        ni = len(self.values)
        self.children[0].append(0)
        self.children[1].append(0)
        self.values.append(x)
        self.counts.append(1)

        li, ri = self.split(self.root, x)
        self.root = self.merge(self.merge(li, ni), ri)

    def delete(self, x):
        li, mri = self.split(self.root, x - 1)
        mi, ri = self.split(mri, x)

        if mi == 0:
            self.root = self.merge(li, ri)
            return

        self.root = self.merge(li, ri)
        return

    def upper_bound(self, x, default=-1):
        i = self.root
        lefts, rights = self.children
        values = self.values
        counts = self.counts
        y = default
        c = counts[i]
        j = 0
        while i != 0:
            if x < values[i]:
                y = values[i]
                c = j + counts[lefts[i]]
                i = lefts[i]
            else:
                j += counts[lefts[i]] + 1
                i = rights[i]
        return y, c

    def lower_bound(self, x, default=-1):
        i = self.root
        lefts, rights = self.children
        values = self.values
        counts = self.counts
        y = default
        c = counts[i]
        j = 0
        while i != 0:
            if x <= values[i]:
                y = values[i]
                c = j + counts[lefts[i]]
                i = lefts[i]
            else:
                j += counts[lefts[i]] + 1
                i = rights[i]
        return y, c

    def get_k_th(self, k, default=-1):
        i = self.root
        children = self.children
        values = self.values
        counts = self.counts
        if counts[i] <= k:
            return default
        j = k
        while i != 0:
            left_count = counts[children[0][i]]
            if left_count == j:
                return values[i]
            elif left_count > j:
                i = children[0][i]
            else:
                j -= left_count + 1
                i = children[1][i]
        return default

    def debug_print(self):
        print('Lefts ', self.children[0])
        print('Rights', self.children[1])
        print('Values', self.values)
        print('Counts', self.counts)
        self._debug_print(self.root, 0)

    def _debug_print(self, i, depth):
        if i != -1:
            self._debug_print(self.children[0][i], depth + 1)
            print('      ' * depth, self.values[i], self.counts[i])
            self._debug_print(self.children[1][i], depth + 1)


def x_check(x_dict, nx, y, d, stack, stacked):
    counter = 0
    if nx in x_dict:
        rbst, lst = x_dict[nx]
        ny, _ = rbst.lower_bound(y - d, y + d + 1)
        while ny <= y + d:
            z = (nx << 32) | ny
            if z not in stacked:
                stack.append(z)
                stacked.add(z)
            rbst.delete(ny)
            ny, _ = rbst.lower_bound(y - d, y + d + 1)
        i = bisect.bisect_left(lst, y - d)
        j = bisect.bisect(lst, y + d)
        counter = j - i
    return counter


def y_check(y_dict, ny, x, d, stack, stacked):
    counter = 0
    if ny in y_dict:
        rbst, lst = y_dict[ny]
        nx, _ = rbst.lower_bound(x - d, x + d + 1)
        while nx <= x + d:
            z = (nx << 32) | ny
            if z not in stacked:
                stack.append(z)
                stacked.add(z)
            rbst.delete(nx)
            nx, _ = rbst.lower_bound(x - d, x + d + 1)
        i = bisect.bisect(lst, x - d)
        j = bisect.bisect_left(lst, x + d)
        counter = j - i
    return counter


n, a, b, *xy = map(int, sys.stdin.buffer.read().split())
xxx = xy[0::2]
yyy = xy[1::2]

x_dict = defaultdict(lambda: [RandomizedBinarySearchTree(), []])
y_dict = defaultdict(lambda: [RandomizedBinarySearchTree(), []])
OFFSET = 10 ** 9
MASK = (1 << 32) - 1
for i in range(n):
    x = xxx[i] - yyy[i] + OFFSET
    y = xxx[i] + yyy[i]
    x_dict[x][0].insert(y)
    y_dict[y][0].insert(x)
    x_dict[x][1].append(y)
    y_dict[y][1].append(x)

for _, lst in x_dict.values():
    lst.sort()
for _, lst in y_dict.values():
    lst.sort()

a -= 1
b -= 1
ax_, ay_ = xxx[a], yyy[a]
bx_, by_ = xxx[b], yyy[b]
ax, ay = ax_ - ay_ + OFFSET, ax_ + ay_
bx, by = bx_ - by_ + OFFSET, bx_ + by_
az = (ax << 32) | ay
bz = (bx << 32) | by
d = max(abs(ax - bx), abs(ay - by))
x_dict[ax][0].delete(ay)
x_dict[bx][0].delete(by)
y_dict[ay][0].delete(ax)
y_dict[by][0].delete(bx)

stack = [az, bz]
stacked = {az, bz}
ans = 0
while stack:
    z = stack.pop()
    y = z & MASK
    x = z >> 32
    ans += x_check(x_dict, x - d, y, d, stack, stacked)
    ans += x_check(x_dict, x + d, y, d, stack, stacked)
    ans += y_check(y_dict, y - d, x, d, stack, stacked)
    ans += y_check(y_dict, y + d, x, d, stack, stacked)

print(ans // 2)
