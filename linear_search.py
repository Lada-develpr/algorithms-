# this code will return the index of the number which was passed to the linear function
# this is a bad and slow implementation of the search algorithms
def linear_search(list, key):
    for idx, item in enumerate(list):
        if key == item:
            return idx
    return -1


list = [int(x) for x in input().split()]
key = int(input())
print(linear_search(list, key))