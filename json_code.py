import json

with open("sample.json") as fh:
    conf = json.load(fh)

print conf
print type(conf)
