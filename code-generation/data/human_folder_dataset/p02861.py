#-*-coding:utf-8-*-
import itertools
import math

def main():
    lists = []
    N= int(input())
    lists=[list(map(int,input().split())) for _ in range(N)]
    ans=0
    length=0
    #permutationsは順列を列挙
    for line in itertools.permutations(lists):
        a = []
        b = []
        for data in line:
            if len(b) ==0:
                b = data
                continue
            else:
                a = b
                b = data
                length = math.sqrt(((b[0]-a[0])**2)+((b[1]-a[1])**2))
                ans+=length
    #factorical=階上の値
    print(ans/math.factorial(N))

if __name__ == "__main__":
    main()