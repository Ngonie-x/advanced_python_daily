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
