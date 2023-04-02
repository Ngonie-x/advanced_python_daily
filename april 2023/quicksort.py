def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


arr = [3, 5, 2, 8, 1, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)
