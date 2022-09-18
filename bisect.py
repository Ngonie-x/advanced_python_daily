import bisect


farm = sorted(['haystack', 'needle', 'cow', 'pig'])
# bisect.bisect(farm, 'needle')


class SortedList(list):
    def __init__(self, iterable):
        super(SortedList, self).__init__(sorted(iterable))
        
    def insort(self, item):
        bisect.insort(self, item)
    
    def extend(self, other):
        for item in other:
            self.insort(item)
            
    @staticmethod
    def append(o):
        raise RuntimeError("Cannot append to a sorted list")
    
    def index(self, value, start=None, stop=None):
        place = bisect.bisect_left(self[start:stop], value)
        
        if start:
            place += start
            
        end = stop or len(self)
        if place < end and self[place] == value:
            return place
        raise ValueError(f"{value} is not in list")
    