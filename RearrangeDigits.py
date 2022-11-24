
def heapsort(array):
    """
    Sorts an array using the heapsort algorithm

    Args:
       array(array): input array to sort
    """

    size = len(array)

    # Build the heap
    for i in range(size, -1, -1):
        heapify(array, size, i)

    # Swap elements
    for j in range(size-1, 0, -1):
        array[j], array[0] = array[0], array[j]
        heapify(array, j, 0)

    
def heapify(array, size, i):
    """
    Represents the array as a heap. Ran recursively

    Args:
       array(array), size(int), i(index): array as an input, length of the array, index
    """

    # Initialise the parent and children
    largest_index = i
    left = 2 * largest_index + 1
    right = 2 * largest_index + 2

    # Compare left and right
    if left < size and array[i] < array[left]:
        largest_index = left

    if right < size and array[largest_index] < array[right]:
        largest_index = right
    
    # Swap largest
    if largest_index != i:

        array[i], array[largest_index] = array[largest_index], array[i]
        heapify(array, size, largest_index)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    if len(input_list) == 1:
        return [input_list[0], 0]

    # Checks if the list needs to be sorted
    for x in range(len(input_list) - 1):

        # While doing the check for if the loop is sorted, it also checks if inputs are valid
        if type(input_list[x]) != int or  type(input_list[x+1]) != int:
            return [-1, -1]

        # Sort the list and break the loop if the current is superior than the next
        if input_list[x] > input_list[x+1]:
            heapsort(input_list)
            break

    small_num = large_num = ''

    # Get the smaller number
    for n in range(len(input_list) - 2, -1, -2):
        small_num += str(input_list[n])

    # Get the larger number
    for n in range(len(input_list) - 1, -1, -2):
        large_num += str(input_list[n])
    
    return [int(large_num), int(small_num)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Regular test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 3, 5, 7, 6], [751, 63]])
test_function([[3, 2, 5, 8, 9], [952, 83]])

# Smaller inputs
test_function([[1, 2, 3], [31, 2]])
test_function([[3, 2, 1], [31, 2]])
test_function([[1, 2], [2, 1]])

# Inputs with lists of size 1
test_function([[1], [1, 0]])
test_function([[0], [0, 0]])

# Larger cases
test_function([[1, 2, 3, 4, 5, 6, 7, 8], [8642, 7531]])
test_function([[3, 6, 7, 1, 4, 5, 0, 2], [7531, 6420]])

# Test cases where duplicates occur
test_function([[1, 3, 3, 5, 7], [731, 53]])
test_function([[8, 5, 1, 2, 8], [851, 82]])

# Null or invalid inputs
test_function([['a', 'b', 'c'], [-1, -1]])
test_function([[1, 2, None], [-1, -1]])
