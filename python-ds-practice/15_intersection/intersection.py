def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    return list(set(l1) & set(l2))


# longer method without built in method
    # set_l2 = set(l2)

    # new_list = []
    # for val in l1:
    #     if val in set_l2:
    #         new_list.append(val)
    
    # return new_list