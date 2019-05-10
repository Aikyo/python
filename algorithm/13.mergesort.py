

def sort(a,b):
    i = j = 0
    c = []
    while i<len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i == len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c


def merge(c):
    if len(c) == 1:
        return c
    mid = len(c) // 2
    left = merge(c[:mid])
    right = merge(c[mid:])
    return sort(left,right)

print(merge([4,3,7,43,2,4,1]))
