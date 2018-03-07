# Adding two dictionaries
capitals = {"USA": "Washington DC", "France": "Paris", "Italy": "Rome"}
more_Capitals = {"Germany": "Berlin", "Russia": "Moscow"}
capitals.update(more_Capitals)
print capitals

# delete item
del capitals["USA"]

# Iterating over key and value both togather
for key, value in capitals.items():
    print key, value

# Merging two dictionaries
x = {"name": "devang", "age": 29}
y = {"points": 25, "likes": ["science", "simulation"]}
z = dict(x, **y)
print z

# Sort dictionary based on value
x = {"a": 1, "b": 2, "c": 3}
print sorted(x.items(), key=lambda x: x[1])
