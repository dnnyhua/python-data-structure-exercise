def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    # Filter the list for only even numbers
    even_numbers = [num for num in nums if num % 2 == 0]

    total = 1
    
    if len(even_numbers) == 0:
        return total
    elif len(even_numbers) > 1:
        for num in even_numbers:
            total *= num     
    return total
