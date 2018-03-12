"""This script demonstrates common list operations in Python"""

# Deleting items from a list
materialProperties = ["conductivity", "absorptance", "transmittance",
                      "emissivity"]
print materialProperties
del materialProperties[0]
print materialProperties
materialProperties.remove("emissivity")
print materialProperties

# Adding items to a list
materialProperties.insert(0, "specific heat")
print materialProperties

# Using enumerate
print "Using enumerate"
for i, j in enumerate(materialProperties):
    print i, j

# Reverse list
print sorted(materialProperties, reverse=True)

# Looping over a list in Reverse
for properties in reversed(materialProperties):
    print properties

# Sorting using a key
print sorted(materialProperties, key=len)
