import itertools

def lcs(x, y):
    # create two lists
    list_x = list(x)
    list_y = list(y)
    
    permutation_x = set(itertools.permutations(list_x))
    permutation_y = set(itertools.permutations(list_y))
    
    num_length = 0
    
    joint_elements = permutation_x & permutation_y
    
    for elemt in joint_elements:
        if len(elemt) >= num_length:
            num_length = len(elemt)
            
    for element in joint_elements:
        if len(element) == num_length:
            return element
        
print(lcs("a", "b"))
print(lcs("a", "a"))
print(lcs("abc", "ac"))
print(lcs("abcdef", "abc"))
print(lcs("abcdef", "acf"))
print(lcs("anothertest", "notatest"))
print(lcs("132535365", "123456789"))
print(lcs("finaltest", "zzzfinallyzzz"))