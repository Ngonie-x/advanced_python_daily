# the decorator pattern
# allows us to 'wrap' an object that provodes core functionality with other objects that alter this functionality. 

#Example
import socket

def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()

def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind('localhost', 2401)
    server.listen(1)
    try:
        while True:
            client, addr = server.accept()
            respond(client)
    finally:
        server.close()
    
# Let's start with a 'logging' decorator. This object outputs any data being sent
# to the server's console before it sends it to the client:

class LogSocket:
    def __init__(self, socket):
        self.socket = socket
        
    def send(self, data):
        print("Sending {0} to {1}".format(data, self.socket.getpeername()[0]))
        self.socket.send(data)
        
    def close(self):
        self.socket.close()
        
# and now instead of calling respond with the socket, we will call with our decorator:
# -> respond(LogSocket(client))

# Example 2
# a second decorator that compresses data using gzip compression whenever send is called:

import gzip
from io import BytesIO

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket
        
    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode='w')
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getValue())
        
    def close(self):
        self.socket.close()
        
        
import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(func.__name__, time.time() - now))
        return return_value
    return wrapper

@log_calls
def test1(a, b, c):
    print('Test 1 called')
    
@log_calls
def test2(a, b):
    print("\ttest3 called")

@log_calls 
def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)



# The observer pattern
# usefult for state monitoring and event handling situations
# this ppatern allows a given object to be monitired by an unknown and dynamic group of "Observer" objects

# Example

class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0
        
    def attach(self, observer):
        self.observers.append(observer)
    
    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()
        
    def _update_observers(self):
        for observer in self.observers:
            observer()
            
# a simple observer object
class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory
         
    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)
            
# simple observer usage
# >>>i = Inventory()
# >>>c = ConsoleObserver(i)
# >>>i.attach(c)
# >>>i.product = "Widget"
# >>>i.quantity = 5

# The strategy pattern
# The pattern implements different solutions to a single problem, each in a different object.
# The client code can then choose the most appropriate implementation dynamically at runtime




from PIL import Image

class TileStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new('RGB', desktop_size)
        num_tiles = [
            o // i + 1 for o, i in zip(out_img.size, in_img.size)
        ]
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(
                    in_img,
                    (
                        in_img.size[0] * x,
                        in_img.size[1] *y,
                        in_img.size[0] * (x+1),
                        in_img.size[1] * (y+1)
                    )
                )
        return out_img



class CenteredStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = Image.new('RGB', desktop_size)
        left = (out_img.size[0] - in_img.size[0]) // 2
        top = (out_img.size[1] - in_img.size[1]) // 2
        out_img.paste(
        in_img,
            (
                left,
                top,
                left+in_img.size[0],
                top + in_img.size[1]
            )
        )
        return out_img

class ScaledStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = Image.open(img_file)
        out_img = in_img.resize(desktop_size)
        return out_img
    
