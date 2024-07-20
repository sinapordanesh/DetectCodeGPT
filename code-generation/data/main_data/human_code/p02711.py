def readinput():
    n=input()
    return n

def main(n):
    if n[0]=='7' or n[1]=='7' or n[2]=='7':
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
