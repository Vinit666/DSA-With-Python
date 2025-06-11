# Sorting in Asending order -->


def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return f"Sorted(By Insertion Sort) List is : {l}"


l = [5, 8, 7, 6, 2, 9, 3, 4, 1, 0, 0, 0, 0, 0, 1]
print(insertion_sort(l))


# Sorting in Decending order -->


def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] < key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return f"Sorted(By Insertion Sort) List is : {l}"


l = [5, 8, 7, 6, 2, 9, 3, 4, 1, 0, 0, 0, 0, 0, 1]
print(insertion_sort(l))
