def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    total = 0

    # range(3) will be 0,1,2
    for i in range(len(matrix)):
        total += matrix[i][1]
        total += matrix[i][-1-i]

    return total



    # ie for m2 above

    # matrix[0][0] # 1
    # matrix[1][1] # 5
    # matrix[2][2] # 9

    # matrix[0][-1-0] # 3
    # matrix[0][-1-1] # 5
    # matrix[0][-1-2] # 7


