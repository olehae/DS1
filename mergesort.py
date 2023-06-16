import matplotlib.pyplot as plt


def assignment(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if len(list_to_sort_by_merge) > 1:
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        left_index = 0
        right_index = 0
        index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                assignment(
                    new_list=list_to_sort_by_merge,
                    i=index,
                    old_list=left,
                    j=left_index,
                )
                left_index += 1
            else:
                assignment(
                    new_list=list_to_sort_by_merge,
                    i=index,
                    old_list=right,
                    j=right_index,
                )
                right_index += 1
            index += 1

        while left_index < len(left):
            list_to_sort_by_merge[index] = left[left_index]
            left_index += 1
            index += 1

        while right_index < len(right):
            list_to_sort_by_merge[index] = right[right_index]
            right_index += 1
            index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
