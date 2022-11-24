
def get_sub_arrays(array):
    """
    Find an optinal middle and divides an array into two. 
    Returns a left and right sub array

    Args:
       array(array), input array to divide
    Returns:
       array: left and right sub arrays
    """

    # (Indexes) Finding the best middle starting point
    mid = len(array) // 2
    upper_mid = mid + 1
    lower_mid = mid - 1

    if type(array[mid]) != int or type(array[upper_mid]) != int or type(array[lower_mid]) != int:
        return None

    # If the middle element > than the next, cut from the next 
    if array[mid] > array[upper_mid]:
        right_arr = array[upper_mid:]
        left_arr = array[:upper_mid]

    # If the middle element > than the previous, cut from  the preveious
    elif array[mid] > array[lower_mid]:
        right_arr = array[lower_mid:]
        left_arr = array[:lower_mid]

    # In all other cases cut from the middle
    else:
        right_arr = array[mid:]
        left_arr = array[:mid]

    return left_arr, right_arr

def search_sub_array(array, number, start, end):
    """
    Recursively searches an array for a number and returns its index

    Args:
       array(array), number(int): array to search, number to find
    Returns:
       int: index of the number
    """

    while start <= end:

        mid = start + (end - start) // 2

        # Return if number is found at the middle
        if array[mid] == number:
            return mid

        # If number is larget than current, increase the index
        if number > array[mid]:
            start = mid + 1

        # Otherwise, lower the index
        else:
            end = mid - 1

    # Return if number is in the range but not in the array    
    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # if 'number' is not a number
    if type(number) != int:
        return None

    if get_sub_arrays(input_list) == None:
        return None

    # Left sub array will contain larger numbers, right sub array will contatin smaller ones
    left_half, right_half = get_sub_arrays(input_list)

    if type(right_half[0]) != int or type(left_half[-1]) != int:
        return None

    # Cases when the number is not in the array
    if number < right_half[0] or number > left_half[-1]:
        return -1

    #print(left_half, right_half)

    # Checks which sub array to start with depending on number size
    if number <= right_half[-1]:

        right_index = search_sub_array(right_half, number, 0, len(right_half) - 1)
        return len(left_half) + right_index

    # If the number is in the larger array
    else:

        left_index = search_sub_array(left_half, number, 0, len(left_half) -1) 
        return left_index


def linear_search(input_list, number):
    for index, element in enumerate(input_list):

        # Added if statement for null values and strings
        if type(element) != int or type(number) != int:
            return None

        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Regular test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test cases for when the lowest number is shifted further left
test_function([[7, 8, 9, 1, 2, 3, 4, 5, 6], 7])
test_function([[7, 8, 9, 1, 2, 3, 4, 5, 6], 1])

# Test cases for even sized arrays
test_function([[4, 5, 6, 1, 2, 3], 2])
test_function([[4, 5, 6, 1, 2, 3], 4])

# Test cases for even sized array where the middle is shifted
test_function([[5, 6, 1, 2, 3, 4], 3])
test_function([[5, 6, 7, 8, 1, 2], 7])

# Test cases for when target is not in the array
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 0])
test_function([[6, 7, 8, 1, 2, 3, 4], 5])
test_function([[4, 5, 6, 1, 2, 3], 7])

# Invalid inputs or array contains not integer elements
test_function([[1, 2, 3], 'a'])
test_function([['a', 'b', 'c'], 1])
test_function([[1, 2, None, 4], 4])