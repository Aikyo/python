def binarysearch(array, key):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        cur = array[middle]
        if key == cur:
            return middle
        else:
            if key < cur:
                right = middle - 1
            else:
                left = middle + 1

lst = [1,3,4,5,6,7,8,9,12,32,45,656,76758,8969679]



index = binarysearch(lst,12)
print(index)





