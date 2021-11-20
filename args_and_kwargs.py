# the *args


def addition(*args):
    result = 0
    for x in args:
        result +=x
    print(result)
    
addition(10, 20, 30)

addition(1, 2, 3, 4, 5)

# the kwargs
def new_order(**kwargs):
    for key, value in kwargs.items():
        print('{} is equal to {}'.format(key, value))
    
new_order(Tea="Green", price=1.8, size="medium", sugar=True)
