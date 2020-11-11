def find_value(array: list, c, start=0, end=None):
    """
    This function takes in a list of values and a comparator or another value. If parameter c is passed as a value then
    the function returns the index of the first occurrence of the value in the list, or None if the list does not
    contain the value. If a callable comparator is passed in as c the function will return the value satisfying the
    comparator. The parameters 'start' and 'end' is set as default to operate through the whole list. However, 'start'
    and 'end' parameters can be defined if one would prefer to perform the search on a sublist of the passed in list.
    """
    if not isinstance(array, list):
        raise TypeError('Input of find_max must be a list!')

    end = len(array) if end is None else end

    if callable(c):
        value = array[start]
        for i in range(start + 1, end):
            value = array[i] if c(value, array[i]) else value

        return value
    else:
        return find_index(array, c, start, end)


def find_index(array: list, c, start=0, end=None):
    """
    This function takes in a list of values and a comparator or another value. If parameter c is passed as a value then
    the function returns the index of the first occurrence of the value in the list. If a callable comparator is passed
    in as c the function will return the index satisfying the comparator. The return value is None if the value is not
    in the list. The parameters 'start' and 'end' is set as default to operate through the whole list. However, 'start'
    and 'end' parameters can be defined if one would prefer to perform the search on a sublist of the passed in list.
    """
    if not isinstance(array, list):
        raise TypeError('Input of find_max must be a list!')

    end = len(array) if end is None else end

    if callable(c):
        index = start
        value = array[index]
        for i in range(start + 1, end):
            if c(value, array[i]):
                index = i
                value = array[index]
    else:
        index = None
        for i in range(start, end):
            if array[i] == c:
                index = i
                break

    return index


class NotSortedError(Exception):
    def __init__(self, message):
        super().__init__(message)


def binary(array: list, value, start=0, end=None):
    """
    Implementation of binary search on a list.
    """
    if not isinstance(array, list):
        raise TypeError("The parameter is not a list")

    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            raise NotSortedError('Provided list is not sorted!')

    end = len(array) if end is None else end

    lp = start
    rp = end-1
    m = (lp + rp) // 2

    while array[m] != value and lp < rp-1:
        if array[m] > value and lp < rp:
            rp = m
        elif array[m] < value and lp < rp:
            lp = m
        else:
            break
        m = (lp + rp) // 2

    return m if lp < rp-1 else None
