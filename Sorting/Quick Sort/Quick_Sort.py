# # Shorting in Ascending order-->


# def partition(l, low, high):
#     pivot = l[low]
#     i = low
#     j = high
#     while i < j:
#         while l[i] <= pivot and i <= high - 1:
#             i += 1
#         while l[j] > pivot and j >= low + 1:
#             j -= 1
#         if i < j:
#             l[i], l[j] = l[j], l[i]
#     l[low], l[j] = l[j], l[low]
#     return j


# def quick_sort(l, low, high):
#     if low < high:
#         p_index = partition(l, low, high)
#         quick_sort(l, low, p_index - 1)
#         quick_sort(l, p_index + 1, high)
#     return l


# l = [2, 6, 8, 3, 9, 4, 5, 2, 6, 1, 0, 1, 1, 2]

# high = len(l) - 1
# print(quick_sort(l, 0, high))


# Shorting in Descending order-->


def partition(l, low, high):
    pivot = l[low]
    i = low
    j = high
    while i < j:
        while l[i] >= pivot and i <= high - 1:
            i += 1
        while l[j] < pivot and j >= low + 1:
            j -= 1
        if i < j:
            l[i], l[j] = l[j], l[i]
    l[low], l[j] = l[j], l[low]
    return j


def quick_sort(l, low, high):
    if low < high:
        p_index = partition(l, low, high)
        quick_sort(l, low, p_index - 1)
        quick_sort(l, p_index + 1, high)
    return l


l = [2, 6, 8, 3, 9, 4, 5, 2, 6, 1, 0, 1, 1, 2]

high = len(l) - 1
print(quick_sort(l, 0, high))
