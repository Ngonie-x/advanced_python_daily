# A recursive function is a function that call itself until it doesn't
# A recursive function needs to have a condition to stop calling itself

#simple recursive function
def count_down(start):
    '''Count down from a number'''
    print(start)
    
    next = start - 1
    if next>0:
        count_down(next)
    
    
# suppose you want to calculate the total of numbers within a range
# method 1, using the range function
def sum(n):
    total = 0
    for index in range(n+1):
        total +=index
    
    return total

result = sum(100)
print(result)


# here is the recursive version of the above function
def nsum(n):
    if n>0:
        return n + nsum(n-1)
    return 0

nresult = nsum(100)
print(nresult)

# same function as above but using the ternary operator
def tsum(n):
    return n + tsum(n-1) if n > 0 else 0