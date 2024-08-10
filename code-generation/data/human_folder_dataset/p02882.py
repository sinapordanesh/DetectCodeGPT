import math

def main():
    a,b,x=map(int,input().split())
    if a**2*b/2<x :
        theta=math.atan(2*(a**2*b-x)/a**3)
    else :
        theta=math.pi/2-math.atan(2*x/(a*b**2))
    print(theta*180/math.pi)

main()