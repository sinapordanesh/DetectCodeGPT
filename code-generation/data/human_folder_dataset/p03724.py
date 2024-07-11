import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	dd=[0]*(n+1)
	for _ in range(m):
		a, b = tin()
		dd[a] += 1
		dd[b] += 1
	for v in dd:
		if v % 2 == 1:
			return 'NO'
	else:
		return 'YES'
		
	
	
#+++++
isTest=False

def pa(*vl):
	if not isTest:
		return
	for v in vl:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)