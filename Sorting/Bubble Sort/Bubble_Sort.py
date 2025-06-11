# Sorting in Acending order -->


def bubble_sort(l):
    for i in range(len(l) - 2, -1, -1):
        for j in range(0, i + 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return f"Sorted(By Bubble Sort) List is : {l}"


l = [5, 8, 7, 6, 2, 9, 3, 4, 1, 0, 0, 0, 0, 0, 1]
print(bubble_sort(l))


# Sorting in Decending order -->


def bubble_sort(l):
    for i in range(len(l) - 2, -1, -1):
        for j in range(0, i + 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return f"Sorted(By Bubble Sort) List is : {l}"


l = [5, 8, 7, 6, 2, 9, 3, 4, 4, 1, 0, 0, 6, 0, 0, 0, 1]
print(bubble_sort(l))
