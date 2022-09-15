def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    count_search_term = [num for num in lst if num == search_term]

    return len(count_search_term)

    # springboard's answer
    # return lst.count(search_term)