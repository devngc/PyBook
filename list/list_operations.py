'''This script demonstrates common list operations in Python'''

# Deleting items from a list
mat = ['conductivity', 'absorptance', 'transmittance', 'emissivity']
print(mat)

# Item removed by Index
del mat[0]
print(mat)

# Specific item removed
mat.remove('emissivity')
print(mat)

# Adding items to a list
mat.insert(0, 'specific heat')
print(mat)

# Using enumerate
print('Using enumerate')
for i, j in enumerate(mat):
    print(i, j)

# Reverse list
print(sorted(mat, reverse=True))

# Looping over a list in Reverse
for properties in reversed(mat):
    print(properties)

# Sorting using a key
print(sorted(mat, key=len))

# Use of a map function
a = list(range(10))


def squared(x):
    return x ** 2


# Using map function
print(list(map(squared, a)))
# Using lambda with Map
print(list(map(lambda x: x**2, a)))
