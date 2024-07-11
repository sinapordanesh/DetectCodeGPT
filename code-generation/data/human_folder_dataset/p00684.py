# AOJ 1102: Calculation of Expressions
# Python3 2018.7.14 bal4u

OVER = 10000

def factor():
	global w, pos
	if buf[pos] == '(':
		pos += 1
		f, v1 = calc()
		if not f: return [f, 0]
		pos += 1
	elif buf[pos] == 'i':
		pos += 1
		v1 = complex(0, 1)
	else:
		v1 = 0
		while pos < w and buf[pos].isdigit():
			v1 = 10*v1 + int(buf[pos])
			pos += 1
			if v1 > OVER: return [False, 0]
	return [True, v1]

def term():
	global w, pos
	f, v1 = factor()
	if not f: return [f, 0]
	while True:
		if pos >= w: break
		if buf[pos] != '*': break
		pos += 1
		f , v2 = factor()
		if not f: return [f, 0]
		v1 *= v2
		if abs(v1.real) > OVER or abs(v1.imag) > OVER: return [False, 0]
	return [True, v1]

def calc():
	global w, pos
	f, v1 = term()
	if not f: return [f, 0]
	while True:
		if pos >= w: break
		op = buf[pos]
		if op != '+' and op != '-': break
		pos += 1
		f , v2 = term()
		if not f: return [f, 0]
		if op == '+': v1 += v2
		else: v1 -= v2
		if abs(v1.real) > OVER or abs(v1.imag) > OVER: return [False, 0]
	return [True, v1]

while True:
	try: buf = list(input().strip())
	except: break
	w, pos = len(buf), 0
	f, ans = calc()
	if not f: print("overflow")
	elif ans.real == 0 and ans.imag == 0: print(0)
	elif ans.real == 0: print(int(ans.imag), 'i', sep='')
	elif ans.imag == 0: print(int(ans.real))
	else: print("{}{:+}i".format(int(ans.real), int(ans.imag)))

