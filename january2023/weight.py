def order_weight(strng:str)-> str:
    # your code
    weights = [i for i in strng.split(' ')]
    weight_dict = {}
    for i in weights:
        weight=0
        for j in i:
            weight+=int(j)
        weight_dict[i] = weight
        
    weight_list = sorted(weight_dict.items(), key=lambda x:x[1])
    sort_dict = dict(weight_list)
    
    
    
    return " ".join(sort_dict.keys())


print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))