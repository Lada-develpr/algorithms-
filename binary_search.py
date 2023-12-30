# this code will return the index of the number which was passed to the binary function
# this is a neat and fast implementation of the search algorithms

def binary_search(list, key):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess > key:
            high = mid - 1
        if guess < key:
            low = mid + 1
        else:
            return mid
    return -1


list = [int(x) for x in input().split()]
key = int(input())
print(binary_search(list, key))