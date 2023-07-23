# read numbers from file and save them to array
array = []
with open('numbers.txt') as file:
    for line in file:
        array.append(int(line.strip()))

# get pivot according to chosen rule
# 0: first element
# -1: last element
# 0.5: median of [first, last, middle element]
def get_pivot_index(input_array, left_p, right_p, option):
    if option == 0:
        return left_p
    if option == -1:
        return right_p
    if option == 0.5:
        first_element = input_array[left_p]
        last_element = input_array[right_p]
        middle_element_index = left_p + (right_p - left_p) // 2
        middle_element = input_array[middle_element_index]
        element_index_map = {first_element: left_p, last_element: right_p, middle_element: middle_element_index}
        median_element = sorted([first_element, last_element, middle_element])[1]
        return element_index_map[median_element]

# Sort an array using in place quicksort, with option to customize pivot choice
def quicksort(input_array, left_p, right_p, pivot_option, total):
    subarray_len =  right_p - left_p + 1
    if pivot_option not in (0, -1, 0.5):
        print('Invalid pivot option')
        return False

    # base case
    if subarray_len in (0,1):
        return
    total[0] += subarray_len - 1
    i = left_p + 1
    j = i

    # choose pivot: 0 for first element, -1 for last, 0.5 for median of three
    pivot_index = get_pivot_index(input_array, left_p, right_p, pivot_option)

    # put pivot as first element
    input_array[left_p], input_array[pivot_index] = input_array[pivot_index], input_array[left_p]
    pivot = input_array[left_p]

    # partition array around pivot
    while j <= right_p:
        curr = input_array[j]
        if curr < pivot:
            input_array[i], input_array[j] = input_array[j], input_array[i]
            i += 1
        j += 1

    # put the pivot in the middle of the 2 partitions
    input_array[left_p], input_array[i - 1] = input_array[i - 1], input_array[left_p]

    # sort left and right part and return full sorted array
    quicksort(input_array, left_p, i - 2, pivot_option, total)
    quicksort(input_array, i, right_p, pivot_option, total)
    return True

# to save how many comparisons are made
total = [0]

quicksort(input_array = array, left_p = 0, right_p = len(array) - 1, pivot_option = 0.5, total= total)
print('Sorted array:', array)
print('Number of comparisons made:', total[0])
