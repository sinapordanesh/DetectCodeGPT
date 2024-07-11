import sys,math,collections
from collections import defaultdict

#from itertools import permutations,combinations
    
def file():
    sys.stdin = open('input.py', 'r')
    sys.stdout = open('output.py', 'w') 
def get_array():
    l=list(map(int, input().split()))
    return l
def get_ints():   
    return map(int, input().split())
    #return a,b
def get_3_ints():   
    a,b,c=map(int, input().split())
    return a,b,c    
def sod(n):
    n,c=str(n),0
    for i in n: 
        c+=int(i)
    return c    
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
  
    return True
def getFloor(A, x):

    (left, right) = (0, len(A) - 1)

    floor = -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            return A[mid]
        elif x < A[mid]:
            right = mid - 1
        else:
            floor = A[mid]
            left = mid + 1
            
    return floor
def chk(aa,bb):
	f=0
	for i in aa:
		for j in bb:
			if(j[0]>=i[0] and j[1]<=i[1]):
				f+=1
			elif(j[0]<=i[0] and j[1]>=i[1]):	
				f+=1
			elif(i[0]==j[1] or i[1]==j[0]):
				f+=1
			else:
				continue
	return f			

#file()
def main():
	s=input()
	print(s[:4]+' '+s[4:])
	



		




				





		


	





        
            
        























    

    
    

        











        
        

        























































                

            







            
            
































        








if __name__ == '__main__':
    main()
