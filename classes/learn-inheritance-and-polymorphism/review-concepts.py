class SortedList(list):
  def __init__(self, values):
    self.extend(values)
    #for num in values:
    #  self.append(num)
    self.sort()

  def append(self, value):
    super().append(value)
    self.sort()

l1 = SortedList([5,4,3,2,1])
print(l1)
l1.append(-1)
print(l1)
