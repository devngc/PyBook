"""This module shows the use of counter as a dictionary."""

from collections import Counter

class1 = ['dog', 'cat', 'camel', 'bird', 'tree', 'car','car']
class2 = ['plane', 'line', 'point', 'car', 'tree']

c1 = Counter(class1)
c2 = Counter(class2)

print(c1)
print(c1['dog'])
print(c1.values())
print(c1.most_common(3))  # Three most common keys
print(sum(c1.values()))
c1.update(c2)
print(c1)
c1.subtract(c2)
print(c1)
print(c1 & c2)