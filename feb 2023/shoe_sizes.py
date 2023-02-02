def pair_of_shoes(shoes):
    shoe_sizes = {}
    
    for type, size in shoes:
        if shoe_sizes.get(size, None) == None:
            shoe_sizes[size] = [type,]
        else:
            shoe_sizes[size].append(type)
            
    for key, values in shoe_sizes.items():
        if len(values)< 2 or values.count(1) != values.count(0):
            return False
    
    return True


print(pair_of_shoes([[0, 23], [1, 23], [1, 23], [0, 23], [0, 23], [0, 23]]))