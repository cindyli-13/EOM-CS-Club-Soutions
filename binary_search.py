
# Binary search repeatedly splits a sorted array in
# half until the value we are looking for is found.


# IMPORTANT NOTE: the array MUST already be sorted in ascending order
# for this function to work
def bin_search(arr, min, max, value):

    # if min is greater than max, then the value we are searching for
    # does not exist in this array (return an error value of -1)
    if min > max:
        return -1

    # find midpoint of min and max
    mid = int((min + max)/2)

    # if arr[mid] is the value we are searching for, we are done
    if arr[mid] == value:
        return mid

    # if arr[mid] is greater than the value we are searching for,
    # set max to mid - 1
    elif arr[mid] > value:
        max = mid - 1

    # if arr[mid] is lesser than the value we are searching for,
    # set min to mid + 1
    else:
        min = mid + 1

    # recursively search within the sub-array
    return bin_search(arr, min, max, value)


# testing (search for x)
x = 0

array = [-6, -5, 0, 1, 2, 3, 5, 10]
print(bin_search(array, 0, len(array) - 1, x))

array = [-14, -10, -4, 0, 2, 4, 5, 9]
print(bin_search(array, 0, len(array) - 1, x))
