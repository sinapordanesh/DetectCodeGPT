def main():
    a,v=map(int,input().split())
    b,w=map(int,input().split())
    t=int(input())
    distance=abs(a-b)
    ve=v-w
    if ve<=0:
        print("NO")
        return
    if distance<=ve*t:
        print("YES")
        return
    else:
        print ( "NO" )
        return
main()