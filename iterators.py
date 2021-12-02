# Python iterators
# Iterators are objects that can be iterated(run or performed again) upon

# An iterator will return data, one element at a time

# A python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol
 
 
# We use the next() function to manually iterate through all the items of an iterator object
# When we reach the end and there is no more data to be returned, it will raise StopIteration

# define list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

#iterate through it using next()
print(next(my_iter))

print(my_iter.__next__())


class PowTwo:
    '''Class to implement an iterator of power of two'''
    
    def __init__(self, max = 0):
        self.max = max
        
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n +=1
            return result
        else:
            raise StopIteration
        
# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for i in PowTwo(5):
    print(i)