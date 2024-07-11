class Activity:
	def __init__(self,s,e):
		self.s=s
		self.e=e

n=int(input())
acts=[]
for i in range(n):
	si,ei=map(int,input().split())
	acts.append(Activity(si,ei))
	
acts.sort(key=lambda x:x.s)
stack=[]
stack.append(acts[0])

for i in range(1,n):
	last = stack[-1]
	acti = acts[i]
	if acti.s > last.e:
		stack.append(acti)
	elif acti.e < last.e:
		stack.pop()
		stack.append(acti)
print(len(stack))

