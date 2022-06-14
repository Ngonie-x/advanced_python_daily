# Bubble sort algorithm

def bubble_sort(list_items, order):
    """Sorts a list using bubble sort

    Args:
        list_items (_type_): _description_
        order (_type_): _description_
    """

    list_size = len(list_items)
    for j in range(list_size-1):
        for i in range(list_size-1):
            if order.lower() == 'a':
                if list_items[i].lower() > list_items[i+1].lower():
                    temp = list_items[i+1]
                    list_items[i+1] = list_items[i]
                    list_items[i] = temp

            elif order.lower() == 'd':
                if list_items[i+1].lower() > list_items[i].lower():
                    temp = list_items[i]
                    list_items[i] = list_items[i+1]
                    list_items[i+1] = temp

            else:
                return print("Invalid order! Etner either 'a' or 'd'")
    return print(list_items)


# Order has two choices; [a]scending or [d]escending order.
list_item = ['v', 'e', 'r', 't', 'i', 'c', 'a', 'l']

# Function call
bubble_sort(list_item, 'a')
