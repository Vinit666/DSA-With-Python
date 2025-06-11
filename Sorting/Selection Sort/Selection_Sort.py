# Sorting in Acending order -->


def selection_sort(l):
    for i in range(0, len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return f"Sorted(By Selection Sort) List is : {l}"


l = [5, 8, 7, 6, 2, 9, 3, 4, 1, 0, 0, 0, 0, 0, 1]
print(selection_sort(l))


# Sorting in Decending order -->


def selection_sort(l):
    for i in range(0, len(l)):
        max_index = i
        for j in range(i + 1, len(l)):
            if l[max_index] < l[j]:
                max_index = j
        l[i], l[max_index] = l[max_index], l[i]
    return f"Sorted(By Selection Sort) List is : {l}"


l = [5, 8, 7, 6, 2, 9, 3, 4, 1, 0, 0, 0, 0, 0, 1]
print(selection_sort(l))
