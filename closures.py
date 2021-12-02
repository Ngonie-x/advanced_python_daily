# Python closures
# A function defined inside another function is called a nested function
# nested functions can access variables of the enclosing scope

def print_msg(msg):
    def printer():
        print(msg)
    
    printer()
    
print_msg('Hello')

# Defining a Closure function
# in the example above, what if the printer() method had been return instead

def print_msg2(msg):
    def printer():
        print(msg)
    
    return printer

another = print_msg2('Hello world')
another()

# this technique in which some data ('Hello world' in this case) gets attached to the code is called closure in python

# When to use closures?

# Closures can avoid the use of global values and provides some form of data hiding. 
# It can also provide an object oriented solution to the problem.

# When there are few methods (one method in most cases) to be implemented in a class, 
# closures can provide an alternate and more elegant solution. But when the number of attributes and 
# methods get larger, it's better to implement a class.


def make_multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier

times3 = make_multiplier_of(3)

times5 = make_multiplier_of(5)

print(times3(3))
print(times5(2))
