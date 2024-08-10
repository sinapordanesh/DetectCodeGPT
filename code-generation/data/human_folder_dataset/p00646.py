# AOJ 1060: No Story
# Python3 2018.6.8 bal4u

MAX = 1000004
ptbl = [ 3,   5,   7,  11,  13,  17,  19,  23,  29,
   31,  37,  41,  43,  47,  53,  59,  61,  67,  71,
   73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
  127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
  179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
  233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
  283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
  353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
  419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
  467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
  547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
  607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
  661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
  739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
  811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
  877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
  947, 953, 967, 971, 977, 983, 991, 997 ]
 
def sieve():
	for p in ptbl:
		for i in range(p*p, MAX, p): tbl[i] = 1
	for i in range(997, MAX, 2):
		if tbl[i] == 0: ptbl.append(i)
 
def prime_factor(n):
	power = []
	if (n & 1) == 0:
		c = 0
		while True:
			n >>= 1
			c += 1
			if n & 1: break
		power.append(c)
	if n <= 1: return power
	if n <= MAX and tbl[n] == 0:
		power.append(1)
		return power
	k = int(n**0.5)
	for p in ptbl:
		if n <= 1: break
		if p > k or (n <= MAX and tbl[n] == 0):
			power.append(1)
			break
		if n % p: continue
		c = 0
		while True:
			n //= p
			c += 1
			if n % p: break
		power.append(c)
	return power

tbl = [0]*MAX
sieve()
while True:
	n = int(input())
	if n == 0: break
	if n == 1:
		print(1)
		continue
	if n <= MAX and (n & 1) and tbl[n] == 0:
		print(2)
		continue
	power = prime_factor(n)
	ans = 1
	for p in power: ans = ans*(1+(p<<1))
	print((ans+1)>>1)
