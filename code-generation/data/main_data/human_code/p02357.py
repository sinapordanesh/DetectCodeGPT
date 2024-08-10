import collections, numbers
import random

def compute(array, window, maximize):
    if not isinstance(window, numbers.Integral):
        raise TypeError()
    if not isinstance(maximize, bool):
        raise TypeError()
    if window <= 0:
        raise ValueError("Window size must be positive")

    result = []
    deque = collections.deque()
    for i, val in enumerate(array):
        val = array[i]
        while len(deque) > 0 and ((not maximize and val < deque[-1]) or (maximize and val > deque[-1])):
            deque.pop()
        deque.append(val)

        j = i + 1 - window
        if j >= 0:
            result.append(deque[0])
            if array[j] == deque[0]:
                deque.popleft()
    return result


class SlidingWindowMinMax(object):

    def __init__(self):
        self.mindeque = collections.deque()
        self.maxdeque = collections.deque()

    def get_minimum(self):
        return self.mindeque[0]

    def get_maximum(self):
        return self.maxdeque[0]

    def add_tail(self, val):
        while len(self.mindeque) > 0 and val < self.mindeque[-1]:
            self.mindeque.pop()
        self.mindeque.append(val)

        while len(self.maxdeque) > 0 and val > self.maxdeque[-1]:
            self.maxdeque.pop()
        self.maxdeque.append(val)

    def remove_head(self, val):
        if val < self.mindeque[0]:
            raise ValueError("Wrong value")
        elif val == self.mindeque[0]:
            self.mindeque.popleft()

        if val > self.maxdeque[0]:
            raise ValueError("Wrong value")
        elif val == self.maxdeque[0]:
            self.maxdeque.popleft()

if __name__ == "__main__":
    n, l = (int(x) for x in input().split())
    array = list((int(x) for x in input().split()))

    answer = compute(array, l, False)
    print(*answer)

