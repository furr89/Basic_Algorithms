def search_num(number):

    # Upper bound will always be equal to or greater than the square root
    upper_bound = number
    lower_bound = 0
    current = 0

    while current*current != number:

        # Keep doing floor division, cutting the range by half
        current = (lower_bound + upper_bound) // 2

        #print("lower:", lower_bound, "upper:", upper_bound) # Print statement used to visualize logarithmic increase

        # If the square root of the middle is equal to the number, return it
        if (current * current) == number:
            return current

        # Handles cases for when the square root is a decimal
        if (lower_bound + 1) == upper_bound:

            # Do a simple division
            current = (lower_bound + upper_bound) / 2

            # And returns the number which is closest 
            if (current * current) > number:
                return lower_bound
            else:
                return upper_bound

        # Set the new range 
        if (current * current) > number:
            upper_bound = current
            
        elif (current * current) < number:
            lower_bound = current

    return current


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Handles cases for when input is either negative, NaN, 0, or 1
    if type(number) != int:
        return None

    if number < 0:
        return None

    if number == 0 or number == 1:
        return number

    # Handles all other cases 
    sqrt_num = search_num(number)

    return sqrt_num


# Regular cases
print ("Pass" if  (2 == sqrt(4)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (12 == sqrt(144)) else "Fail")

# Large numbers to test logarithmic increase in computation
print ("Pass" if  (20 == sqrt(400)) else "Fail")
print ("Pass" if  (30 == sqrt(900)) else "Fail")

# 0s and 1s
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")

# Decimal results
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (7 == sqrt(48)) else "Fail")

# Negative tests
print ("Pass" if  (0 == sqrt(-0)) else "Fail")
print ("Pass" if  (None == sqrt(-16)) else "Fail")

# Test cases where inputs are not ints
print ("Pass" if  (None == sqrt("12")) else "Fail")
print ("Pass" if  (None == sqrt('c')) else "Fail")
print ("Pass" if  (None == sqrt(None)) else "Fail")
