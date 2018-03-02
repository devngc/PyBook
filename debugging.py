import pdp

values = range(1, 11)
for val in values:
    mysum = 0
    mysum += val
    pdp.set_trace()
print mysum
