#FIFO
from queue import Queue

waiting_list = Queue()

# putting data into the queue
waiting_list.put("Ahmed")
waiting_list.put("Ibra")
waiting_list.put("Marcelo")
waiting_list.put("Joe")

print(waiting_list.get())
print(waiting_list.get())
print(waiting_list.get())


# queue with maximum size attribute
lineup  = Queue(maxsize=3)
lineup.put("one")
lineup.put("two")
lineup.put("three")

print(lineup.full())
print(lineup.get())
print(lineup.get())
print(lineup.get())

print(lineup.empty())


# LIFO

from queue import LifoQueue
stack = LifoQueue(maxsize=3)

stack.put("one")
stack.put("two")
stack.put("three")

print(stack.full())

print(stack.get())
print(stack.get())
print(stack.get())

# Priority Queue
from queue import PriorityQueue

heap = PriorityQueue()

heap.put((2, "two"))
heap.put((1, "one"))
heap.put((4, "four"))
heap.put((3, "three"))

while not heap.empty():
    print(heap.get())