# this is a bubble sorting algorithm that sorts list in quadratic time

# count = 0
def bubble_sort(list):
    for run in range(len(list)-1):
        for i in range(len(list)-1-run):
            if list[i] > list[i+1]:
                # count += 1
                list[i], list[i+1] = list[i+1], list[i]


list = [int(x) for x in input().split()]
bubble_sort(list)
print(list)