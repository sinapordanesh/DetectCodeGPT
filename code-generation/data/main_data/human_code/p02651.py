import sys
input = sys.stdin.readline

class BaseXor:
    def __init__(self):
        self.size = 0
        self.base = []
    
    def base_calculate(self, x, b):
        return min(x, x ^ b)

    def make_base(self, x):
        for b in self.base:
            x = self.base_calculate(x, b)
        return x
    
    def change_base(self, x):
        for i in range(self.size):
            self.base[i] = self.base_calculate(self.base[i], x)
    
    def judge_linearly_dependent(self, x, value=False):
        x = self.make_base(x)
        res = True if x else False
        res = (res, x) if value else res
        return res
    
    def add_base(self, x):
        judge, x = self.judge_linearly_dependent(x, value=True)
        if judge:
            self.change_base(x)
            self.base.append(x)
            self.size += 1
            return True
        return False

def solve(n, a, s):
    base = BaseXor()
    judge = False
    for i in range(n-1, -1, -1):
        x = s[i]
        if x == "0":
            base.add_base(a[i])
        else:
            judge = base.judge_linearly_dependent(a[i])
            if judge:
                break
    
    res = 1 if judge else 0
    return res

def main():
    t = int(input())
    ans = [0]*t
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = input()
        res = solve(n, a, s)
        ans[i] = res
    print(*ans, sep="\n")
    
if __name__ == "__main__":
    main()

