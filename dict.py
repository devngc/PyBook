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