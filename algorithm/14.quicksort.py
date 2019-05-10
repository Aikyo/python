
def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]
    array[low] = key
    return low



array = [4,3,1,76,9,0]
quick_sort_standord(array,0,5)
print(array)