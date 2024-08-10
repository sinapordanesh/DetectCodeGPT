#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problems 1301
Problem G: Malfatti Circles
"""
import math
def main():
    while True:
        x1, y1, x2, y2, x3, y3 = map(int,input().split())
        if  x1 == y1 == x2 == y2 == x3 == y3 == 0:
            break
        
        a = math.sqrt( (x2-x3)*(x2-x3) + (y2-y3)*(y2-y3) ) # aの長さ
        b = math.sqrt( (x1-x3)*(x1-x3) + (y1-y3)*(y1-y3) ) # bの長さ
        c = math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ) # cの長さ

        cosA = round((b*b + c*c - a*a),10) / round(2*b*c,10) # 余弦定理
        cosB = round((a*a + c*c - b*b),10) / round(2*a*c,10) # 余弦定理
        cosC = round((a*a + b*b - c*c),6) / round(2*a*b,10) # 余弦定理
        
        A = math.degrees(math.acos(cosA)) # bcの角度
        B = math.degrees(math.acos(cosB)) # acの角度
        C = math.degrees(math.acos(cosC)) # abの角度
        
        S = 1/2*a*c*math.sin(math.radians(B)) # 三角形の面積
        r = 2*S / (a+b+c) # 内接円半径
        
        tanA4 = round(math.tan(math.radians(A)/4),10) # tan(A/4)
        tanB4 = round(math.tan(math.radians(B)/4),10) # tan(B/4)
        tanC4 = round(math.tan(math.radians(C)/4),10) # tan(C/4)
        
        r1 = ((1+tanB4)*(1+tanC4))/(2*(1+tanA4))*r
        r2 = ((1+tanC4)*(1+tanA4))/(2*(1+tanB4))*r
        r3 = ((1+tanA4)*(1+tanB4))/(2*(1+tanC4))*r
        
        print(r1, r2, r3)

if __name__ == "__main__":
    main()
