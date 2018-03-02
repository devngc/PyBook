import yaml
import json

myDict = {"a": 1, "b": 2, "c": 3}
myList = range(1, 6)
myTuple = ("x", "y", "z")

loaded_yaml = yaml.dump(myDict, default_flow_style=False)
print loaded_yaml
print yaml.dump(myList, default_flow_style=False)
print yaml.dump(myTuple, default_flow_style=False)

print "More complex object now \n"
myObj = (
    [1, 2, 3, 4, 5],
    {"a": 1, "b": 2, "c": 3},
    [
        {"x": 98, "y": 99, "z": 100},
        3,
        4
    ],
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
)
print yaml.dump(myObj, default_flow_style=False)

print "Now loading a yaml file \n"
with open("config.yaml") as fh:
    struct = yaml.load(fh)
print struct    # This output is not very readable. So,json will be used
print json.dumps(struct, indent=4, separators=(",", ":"))
