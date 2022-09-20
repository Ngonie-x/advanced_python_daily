from typing import TypeVar, Generic, List
T = TypeVar("T")

class Stack:
    def __init__(self) -> None:
        self.container: List[T] = []
        
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self)-> T:
        return self._container.pop()
    
    def __repr__(self) -> T:
        return repr(self._container)