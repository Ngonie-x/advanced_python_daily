def max_mirror(arr):
    arr_length = len(arr)
    rev_arr = arr.reverse()

    if arr_length < 2:
        return 0

    if arr == rev_arr:
        return arr_length
