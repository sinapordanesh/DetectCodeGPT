# AOJ 1602: ICPC Calculator
# Python3 2018.7.13 bal4u

def calc(lvl, idx):
	c = e[idx][lvl]
	if c.isdigit(): return [int(c), idx+1]
	lvl, idx = lvl+1, idx+1
	x = 0 if c == '+' else 1
	while idx < len(e):
		f = i = 0
		while i < len(e[idx]) and i < lvl:
			if e[idx][i] != '.': break
			i += 1
		if i < lvl: break
		if e[idx][i].isdigit(): y, f = int(e[idx][i]), 1
		else: y, idx = calc(lvl, idx)
		x = x+y if c == '+' else x*y
		if f: idx += 1
	return [x, idx]

while True:
	n = int(input())
	if n == 0: break
	e = [list(input()) for i in range(n)]
	print(calc(0, 0)[0])

