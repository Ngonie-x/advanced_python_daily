# a decorator is a function that takes another function as an argument and extends it's behaviour without
# changing the original function explicitly


# let's start with a simple python decorator



# suppose you need to format the net proce using the usd currency
def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
        
    return wrapper

@currency
def net_price(price, tax):
    '''
        calculate the net price from price and tax
    '''
    return price * (1+tax)

# net_price = currency(net_price)
print(net_price(100, 0.05))