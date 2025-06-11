def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    return result


def Merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    left = Merge_sort(left_half)
    right = Merge_sort(right_half)
    return merge_array(left, right)


array = [2, 6, 8, 3, 9, 4, 5, 2, 6, 1, 0, 1, 1, 2]
print(Merge_sort(array))
