class Card:
	def __init__(self, mark, num, order):
		self.mark = mark
		self.num = num
		self.order = order
	def __str__(self):
		return self.mark + ' ' + str(self.num)

def quick_sort(cards, p, r):
	if p < r:
		q = partition(cards, p, r)
		quick_sort(cards, p, q - 1)
		quick_sort(cards, q + 1, r)

def partition(cards, p, r):
	x = cards[r].num
	i = p - 1
	for j in range(p, r):
		if cards[j].num <= x:
			i += 1;
			swap(cards, i, j)
	swap(cards, i + 1, r)
	return i + 1

def swap(cards, i, j):
	tmp = cards[i]
	cards[i] = cards[j]
	cards[j] = tmp

def check_stability(cards):
	for i in range(1, len(cards)):
		c1 = cards[i-1]
		c2 = cards[i]
		if c1.num == c2.num and c1.order > c2.order:
			return False
	return True

n = int(input())
cards = []
for i in range(n):
	mark, num = map(str, input().split())
	cards.append(Card(mark, int(num), i))

quick_sort(cards, 0, n - 1)
stable = check_stability(cards)
if stable == True:
	print('Stable')
else:
	print('Not stable')
for i in range(n):
	print(cards[i])

