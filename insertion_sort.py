# this is an insertion sorting algorithm that sorts list in quadratic time

def insertion_sort(list):
        cur = i
        j = i - 1
        while j >= 0 and cur < list[j]:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = cur


list = [int(x) for x in input().split()]
insertion_sort(list)
print(list)