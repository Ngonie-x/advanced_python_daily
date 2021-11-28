import math

class Point:
    'Represents a point in two-dimansional geometric coordinates'
    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y coordinates can 
        be specified. If they are not, the point defaults to the origin'''
        self.move(x, y)
    
    def move(self, x, y):
        '''Move the point to a new location in 2d space'''
        self.x = x
        self.y = y
        
    def reset(self):
        'Reset the point to the geometric origin: 0, 0'
        self.move(0, 0)
        
    def calculate_distance(self, other_point):
        '''Calculate the distance from this point to the other point given as the 
        parameter'''
        return math.sqrt(
            (self.x - other_point.x)**2 + (self.y - other_point.y)**2
            )
      
      
      
class ContactList(list):
    def search(self, name):
        '''Return all the contacts that contain the search value in theor name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts  
        
class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send '{}' order to '{}'".format(order, self.name))
        
        
    
        
class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
      
      
class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone    
      
        
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key)> len(longest):
                longest = key
        return longest
    
    
class AudioFile:
    def __init__(self, filename):
        if not filename.endwith(self.ext):
            raise Exception("Invalid file format")
        
        self.filename =filename
        

class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print("playing {} as mp3".format(self.filename))
        
class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))
        
class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))