time = -1
place = ["a","b","c","d","e","f","g","h","i"]
empty_count={}
for i in place:
	empty_count[i] = 0
count_d = empty_count.copy()	

def reset():
	global d
	global count_d
	d={"a":["a","a","b","d"],"b":["a","e","c","b"],"c":["b","f","c","c"],"d":["a","e","g","d"],"e":["b","d","f","h"],"f":["c","e","i","f"],"g":["d","h","g","g"],"h":["g","e","i","h"],"i":["f","h","i","i"]}
	count_d = empty_count.copy()
	
	
def pre_set(start_place,fix_place):
	global d
	global count_d
	for i in place:
		d[i] = list(("").join(d[i]).replace(fix_place,i))
	count_d[start_place] = 1
	
def repeat(time):
	global count_d
	for i in range (time):
		new_count_d = empty_count.copy()
		old_count_d = count_d.copy()
		for j in place:
			for k in d[j]:
				new_count_d[k] += old_count_d[j]
		count_d = new_count_d.copy() 

while time != 0:
	time = int(raw_input())
	if time == 0:
		break
	else:
		info_pre = raw_input().split()
		info = []
		for i in info_pre:
			info.append(i.lower())
		
	reset()
	pre_set(info[0],info[2])
	repeat(time)
	print (count_d[info[1]])/float((4**time))
	
		
	