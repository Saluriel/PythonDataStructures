def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    my_list = list(range(1, num+1, 1))
    # create a list with the range of the number
    final_list = []

    for ints in my_list:
        answer = num/ints
        if (answer - int(answer) == 0):
            final_list.append(int(answer))
    return final_list

