def swap(array: list, i: int, j: int):
    if not isinstance(array, list):
        raise TypeError("Must provide a list for bubble sort function")
    if not isinstance(i, int) or not isinstance(j, int):
        raise TypeError("i, and j parameters must be of type int")

    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def bubble(array: list, start = 0, end = None):
    if not isinstance(array, list):
        raise TypeError("Must provide a list for bubble sort function")

    end = len(array) if end is None else end

    for i in range(start+1, end):
        for j in range(start+1, end - i):
            if array[j-1] > array[j]:
                swap(array, j-1, j)