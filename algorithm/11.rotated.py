def rotate(num,pivot):
    return num[pivot:] + num[:pivot]

print(rotate([1,2,3,4,5,6],3))