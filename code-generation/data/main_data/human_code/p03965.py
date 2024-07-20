import sys
def input(): return sys.stdin.readline().strip()

def main():
    S = input()
    gp = [0, 0]
    ans = 0
    for c in S:
        if gp[0] > gp[1] and c == 'g':
            ans += 1
            gp[1] += 1
        elif gp[0] > gp[1] and c == 'p':
            gp[1] += 1
        elif c == 'g':
            gp[0] += 1
        else:
            ans -= 1
            gp[0] += 1
    print(ans)




if __name__ == "__main__":
    main()
