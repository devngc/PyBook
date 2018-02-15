"""This file demonstrates the use of sets in Python"""

# The set is an unordered list of unique members
a = set(" I am devang")
b = set("I like work a lot")

result01 = a - b    # Members in set a but not in set b
result02 = a | b    # Members in set a or set b or both
result03 = a ^ b    # Mebers in set a or set b but not both
result04 = a & b    # Members in both sets

print result01
print result02
print result03
print result04

# Intersecting List
c = range(1, 21)
d = range(11, 21)
e = [c, d]
sete = [set(item) for item in e]
intersection = set.intersection(*sete)
print sorted(intersection)
