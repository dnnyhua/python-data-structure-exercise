def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    dict_1 = {}
    dict_2 = {}

    for num in str(num1):
        if num in dict_1: 
            dict_1[num] += 1
        else:
            dict_1[num] = 1

    for num in str(num2):
        if num in dict_2: 
            dict_2[num] += 1
        else:
            dict_2[num] = 1

    return dict_1 == dict_2


# Springboard's Answer

# Uses two functions

# def freq_counter(coll):
#     """Returns frequency counter mapping of coll."""

#     counts = {}

#     for x in coll:
#         counts[x] = counts.get(x, 0) + 1

#     return counts


# def same_frequency(num1, num2):
#     """Do these nums have same frequencies of digits?

#         >>> same_frequency(551122, 221515)
#         True

#         >>> same_frequency(321142, 3212215)
#         False

#         >>> same_frequency(1212, 2211)
#         True
#     """

#     return freq_counter(str(num1)) == freq_counter(str(num2))
