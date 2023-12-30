# this is a selection sorting algorithm that sorts list in quadratic time

def find_smallest(list):
    smallest = list[0]
    smallest_idx = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_idx = i
    return smallest_idx


def selection_sort(list):
    result_list = []
    for i in range(len(list)):
        smallest = find_smallest(list)
        result_list.append(list.pop(smallest))
    return result_list


list = [int(x) for x in input().split()]
print(selection_sort(list))