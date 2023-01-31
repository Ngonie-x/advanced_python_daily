# Made use of reduce to calculate the sum of numbers in a list

from functools import reduce
def get_sum_of_digits(num):
    num_str = str(num)
    nums = [int(i) for i in list(num_str)]
    
    return reduce(lambda a, b: a+b, nums)