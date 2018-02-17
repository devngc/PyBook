# Dict comprehension
square3_dict = {i: i**2 for i in range(30) if i % 3 == 0}
print square3_dict

# Transpose dictionary
capitals = {"USA": "Washington DC", "France": "Paris", "Italy": "Rome"}
capitals_first = {capitals[key]: key for key in capitals}
print capitals_first
