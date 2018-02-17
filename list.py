
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
for i, j in enumerate(materialProperties):
    print i, j
