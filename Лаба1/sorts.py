def bubble_sort(array):  # пузырьком

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def cocktail_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while swapped:
        swapped = False
        for i in range(start_index, end_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        end_index = end_index - 1

        if not swapped:
            break
        swapped = False
        for i in range(end_index - 1, start_index - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start_index = start_index + 1
    return array


def merge_sort(array):  # слиянием

    if len(array) >= 2:
        middle = int(len(array) / 2)
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1

            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

        return array
    return array
