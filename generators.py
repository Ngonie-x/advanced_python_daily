# A generator is a function that returns an object(iterator) which we can iterate over(one value at a time)
# If a function contains at least one yield statement, it becomes a generator function

# the difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successice calls

# simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    
    yield n
    
    n+=1
    print('This is printed second')
    yield n
    
    n+=1
    print('This is printed last')
    yield n
    
a = my_gen()
next(a)
next(a)
next(a)


for item in my_gen():
    print(item)
    
# generator to reverse a string

def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]
        

for char in rev_str('hello'):
    print(char)
    
# Python Generator Expression

my_list = [1, 3, 6, 10]

# square each item using list comprehension
list_ = [x**2 for x in my_list]

# generator expressions are surrounded by parenthesis()
generator = (x**2 for x in my_list)

print(list_)
print(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


def PowTwoGen(max=0):
    n=0
    while n<max:
        yield 2**n
        n+=1
       
       
# some cool code coming up
# it's called pipelining generators! 
        
def fibo_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
        
def square(nums):
    for num in nums:
        yield num**2
        
print(sum(square(fibo_numbers(10))))