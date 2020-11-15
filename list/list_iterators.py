import itertools


def func(x):
    return True if x % 4 == 0 else False


# This will cycle through the list and start again at the top
names = ['John', 'Don', 'Kohn']
cycle1 = itertools.cycle(names)
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print('')

# Gives an infinite items with an increment
count1 = itertools.count(100, 10)
print(next(count1))
print(next(count1))
print(next(count1))
print(next(count1))
print('')

# Accumulates value at each step
vals = [10, 20, 30, 40, 50, 40, 30]
acc = itertools.accumulate(vals)
print(list(acc))
print('')

# Chaining items on two lists
z = itertools.chain('ABCD', '1234')
print(list(z))
print('')

# Filtering using
print(list(itertools.dropwhile(func, vals)))
print(list(itertools.takewhile(func, vals)))
