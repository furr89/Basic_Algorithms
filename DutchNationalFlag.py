
def sort_012(input_list):
    """
    Sorts an array of 3 elements, 0, 1, 2. 

    Args:
        input_list(Array): list to sort

    Returns:
        input_list(Array): sorted array 
    """

    # Save the positions for 0 and 2
    num0_pos = 0
    num2_pos = len(input_list) - 1

    current = 0
    while current <= num2_pos:

        # Handle non integers
        if type(input_list[current]) != int:
            return None

        # If there is a number above 2, return null
        if input_list[current] > 2:
            return None

        # If the number at current index is 0
        if input_list[current] == 0:

            # Insert to the front, and increment the next position for 0
            input_list[current] = input_list[num0_pos]
            input_list[num0_pos] = 0

            num0_pos += 1
            current += 1

        # If the number is 2
        elif input_list[current] == 2:

            # Insert at the end and decrement the end's position
            input_list[current] = input_list[num2_pos]
            input_list[num2_pos] = 2

            num2_pos -= 1

        # If it is 1, leave it
        else:
            current += 1

    return input_list


def test_function(test_case):

    # Added this if statement for null values
    if sort_012(test_case) == None:
        print("Null")
        return

    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Additional test cases
test_function([2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
test_function([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])
test_function([1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2])
test_function([1, 1, 1, 1, 1, 2, 2, 2, 0])

# Small sized list test cases
test_function([0, 0])
test_function([2, 0])
test_function([1])
test_function([])

# All tests below should return None

# Test cases with numbers other than 0, 1, 2
test_function([0, 1, 2, 0, 2, 1, 3]) 
test_function([4, 5]) 

# Test cases with array elements not an int
test_function([0, 's'])
test_function([None])
