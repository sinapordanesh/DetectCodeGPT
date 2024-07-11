def f(y, m):
	if y in range(1, 13) and m in range(1, 13):
		return "AMBIGUOUS"
	if m in range(1, 13):
		return "YYMM"
	if y in range(1, 13):
		return "MMYY"
	return "NA"
  
S = input()
y, m = int(S[:2]), int(S[2:])
print(f(y, m))
  
