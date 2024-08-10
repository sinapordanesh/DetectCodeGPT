# from functools import lru_cache

# @lru_cache
# def grundy(s):
#     if len(s) == 2:
#         return 0
#     gs = set()
#     for i in range(1, len(s) - 1):
#         if s[i - 1] == s[i + 1]:
#             continue
#         gs.add(grundy(s[:i] + s[i + 1:]))
#     for i in range(100):
#         if i not in gs:
#             return not (i == 0)

def win_first(s):
    return ((s[0] == s[-1]) + len(s)) % 2

# def test():
#     for i in range(1000000):
#         s = str(i)
#         for c1, c2 in zip(s[:-1], s[1:]):
#             if c1 == c2:
#                 break
#         else:
#             assert win_first(s) == grundy(s)

def main():
    print("First" if win_first(input()) else "Second")

main()