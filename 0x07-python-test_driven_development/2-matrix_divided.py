#!/usr/bin/python3

"""divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Returns a new matrix of divided values of matrix

    Values are to be divided by div

    Raises:
        TypeError: if div is not a number
                    if an element of matrix is not an int or float
                    if each row of matrix is not the same

        ZeroDivisionError: if div is zero
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    b = 0 
    final = []
    lent = len(matrix[0])

    for i in matrix:
        """checking to see if all elements are integers or floats"""
        for x in i:
            if type(x) != int and type(x) != float:
                b = b + 1
        if b > 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        """checking to see if the rows are of the same length"""
        if len(i) != lent:
            raise TypeError("Each row of the matrix must have the same size")

        base = list(map((lambda x: round((x / div), 2)),i))
        final.append(base)
    return final

