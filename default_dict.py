from collections import defaultdict
from functools import partialmethod

new_defaultdict = defaultdict(int)
print(new_defaultdict[4])

set_defaultdict = defaultdict(set)


set_defaultdict['five'].add(5)
set_defaultdict['ten'].add(10)
set_defaultdict['five'].add(5)
set_defaultdict['ten'].add(10)
set_defaultdict['fifteen']

print(dict(set_defaultdict.items()))


list_defaultdict = defaultdict(list)

list_defaultdict['five'].append(5)
list_defaultdict['ten'].append(10)
list_defaultdict['five'].append(5)
list_defaultdict['ten'].append(10)
list_defaultdict['fifteen']
print(list_defaultdict.items())