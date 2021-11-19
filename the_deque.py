from collections import deque

waiting_list = deque()

waiting_list.append('Ahmed')
waiting_list.append('Fred')
waiting_list.append('ronald')
waiting_list.append('Ibrahim')

print(waiting_list)

print(waiting_list.popleft())

# clear the list
waiting_list.clear()
print(waiting_list)