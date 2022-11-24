
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    min_max = []

    # Return an empty tuple if the input array contains no numbers
    if len(ints) == 0:
        return ()

    # Iterate through list
    for i in range(len(ints)):

        if type(ints[i]) != int:
            return None

        # Handle the first two numbers
        if i == 0:

            min_max.append(ints[i])

        elif i == 1:
            
            # If it is greater than the first num, append it
            if ints[i] > min_max[0]:
                min_max.append(ints[i])

            # Otherwise, add it at index 0 and shift the other
            else:
                min_max.insert(0, ints[i])

        elif i >= 2:

            # Only make changes if i greater than the max number
            if ints[i] > min_max[1]:
                min_max[1] = ints[i]

            # Or lower than the lowest number
            elif ints[i] < min_max[0]:
                min_max[0] = ints[i]

    # Handles cases when input array contains a single number
    if len(min_max) == 1:

        num = min_max[0]

        if num >= 0:
            min_max = [0, num]

        else:
            min_max = [num, 0]

    #print(min_max)
    return (min_max[0], min_max[1])


# Random list test case of ten integers
import random

l = [i for i in range(0, 10)]  # A list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Regular test cases
l = [0, 1, 2, 3, 4, 5]
print ("Pass" if ((0, 5) == get_min_max(l)) else "Fail")

l = [7, 5, 3, 1, 6, 4, 2, 0]
print ("Pass" if ((0, 7) == get_min_max(l)) else "Fail")

l = [12, 10, 6, 8, 5, 14, 17, 25, 22]
print ("Pass" if ((5, 25) == get_min_max(l)) else "Fail")

l = [0, 1, 3, 5, 7, -3]
print ("Pass" if ((-3, 7) == get_min_max(l)) else "Fail")

# Inputs with a single element in the array
l = [0]
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = [2]
print ("Pass" if ((0, 2) == get_min_max(l)) else "Fail")

l = [-3]
print ("Pass" if ((-3, 0) == get_min_max(l)) else "Fail")

l = []
print ("Pass" if (() == get_min_max(l)) else "Fail")

# Invalid inputs where anything other than ints are present
l = [1, 2, '3']
print ("Pass" if (None == get_min_max(l)) else "Fail")

l = [0, None, 3]
print ("Pass" if (None == get_min_max(l)) else "Fail")