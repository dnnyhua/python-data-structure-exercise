def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    counter = {}

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    # max() will iterate through the dictionary and will return the key with highest value
    return max(counter, key= counter.get)