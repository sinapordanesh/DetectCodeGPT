import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def cc(al, start):
	mc = 0
	is_m = start
	pre_total_sum=0
	for v in al:
		pre_total_sum += v
		if is_m*pre_total_sum <= 0:
			mc += abs(pre_total_sum-is_m)
			pre_total_sum = is_m
		is_m *= -1
	#pa(mc)
	return mc

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	al = lin()
	ret = min(cc(al, -1), cc(al, 1))
	return ret
	
	
	
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