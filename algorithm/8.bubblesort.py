def bubblesort(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]>num[j]:
                num[i],num[j] = num[j],num[i]
    return num
print(bubblesort([3,2,1,-10,23,-34]))
