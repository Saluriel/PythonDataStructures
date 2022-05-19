def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    new_list = []

    for item in lst:
        if isinstance(item, list):
            new_list.append(True)
        else:
            new_list.append(False)

    if False in new_list:
        return False
    else: 
        return True
