def remove_slimes(ls):
	l = [ls[0]]
	for i in range(1, len(ls)):
		if ls[i-1] != ls[i]:
			l.append(ls[i])
	return len(l)

n = int(input())
s = input()
cnt = 1
if len(s) != 1:
	cnt = remove_slimes(list(s))
print(cnt)