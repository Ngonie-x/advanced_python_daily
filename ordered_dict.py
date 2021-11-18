from collections import OrderedDict

# create dict
new_dict = {'apple': 3, 'banana': 7, 'cherry': 4}

new_ordered_dict = OrderedDict()
print(new_ordered_dict)

# ordered dict from regular dictionary
new_orderedDict = OrderedDict(new_dict)
print(new_orderedDict)

# add new item
new_orderedDict['fig'] = 5
print(new_orderedDict)

# replace item in a dict
new_orderedDict['apple'] = 10
print(new_orderedDict)

# delete values
new_orderedDict.pop("cherry")
print(new_orderedDict)

# move item to the end of the ordered dictionary
new_orderedDict.move_to_end('apple')
print(new_orderedDict)

# reverse iteration
for item in reversed(new_orderedDict):
    print(item)