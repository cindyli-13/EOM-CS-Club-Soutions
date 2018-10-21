
# Bubble sort is a sorting algorithm that repeated
# swaps adjacent elements in an array until the array is
# sorted.

# The following two methods are two different ways of
# implementing bubble sort. The first does not use recursion
# whereas the second does.


# Non-recursive
def sort(arr):

    # starting with last value in array, loop until first value
    for i in range(len(arr), 0, -1):

        # boolean flag for checking if the array is already
        # sorted (not needed, but improves efficiency)
        is_sorted = True

        for j in range(i - 1):

            # if element before is greater than element after,
            # then swap the elements
            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False

        if is_sorted:
            return arr

    return arr


# Recursive
def sort_recur(arr):

    # if the array's length is 1 or less then it is already sorted
    if len(arr) <= 1:
        return arr

    else:

        # loop from first element to second last
        for i in range(len(arr) - 1):

            # if element before is greater than element after,
            # then swap the elements
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # recursively sort the sub array of the first to the second
        # last element, and combine that array with the last element
        arr = sort_recur(arr[:-1]) + [arr[-1]]
        return arr


# testing
array = [3, 5, 0, 1, 1, -5, 10, 2, -6]
print(sort(array))

array = [5, -10, -4, 2, 0, 9, -14, 4]
print(sort_recur(array))

