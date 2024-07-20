class TemplateTree:
  def __init__(self, iterable):
    self.iter_size = self.get_size(iterable)
    self.size = self.iter_size * 2 - 1
    self.value = [None] * self.size
    for i, v in enumerate(iterable):
      self.value[self.iter_size + i - 1] = v
    self.set_value(0)
    self.range = [None] * self.size
    self.set_range(0, 0, self.iter_size - 1)
  
  def get_size(self, iterable):
    ret = 1
    x = len(iterable)
    while ret < x:
      ret *= 2
    return ret
  
  def set_range(self, x, left, right):
    self.range[x] = (left, right)
    if left != right:
      self.set_range(x * 2 + 1, left, (right + left) // 2)
      self.set_range(x * 2 + 2, (right + left) // 2 + 1, right)

  def set_value(self, x):
    if x >= self.iter_size - 1:return self.value[x]
    a = self.set_value(x * 2 + 1)
    b = self.set_value(x * 2 + 2)
    if a == None and b == None:
      self.value[x] = None
    elif a == None:
      self.value[x] = b
    elif b == None:
      self.value[x] = a
    else:
      self.value[x] = a
    return self.value[x]

  def update(self, x, add, left, right):
    x_left, x_right = self.range[x]
    if right < x_left or x_right < left:
      pass
    elif left <= x_left and x_right <= right:
      self.value[x] += add
    else:
      self.update(x * 2 + 1, add, left, right)
      self.update(x * 2 + 2, add, left, right)
  
  def query(self, x, total):
    if x < 0:return total
    total += self.value[x]
    return self.query((x - 1) // 2, total)

  def print_tree(self):
    print(self.value)
    print(self.range)

n, q = map(int, input().split())
tree = TemplateTree([0] * n)

for _ in range(q):
  lst = list(map(int, input().split()))
  if lst[0] == 0:
    s, t, x = lst[1:]
    tree.update(0, x, s - 1, t - 1)
  else:
    i = lst[1]
    print(tree.query(tree.iter_size - 1 + i - 1, 0))


