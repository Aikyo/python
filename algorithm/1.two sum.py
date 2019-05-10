"""
num = [1,2,3,4,5]
target = 5
return (0,3)


"""
def twoSum(num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i
        else:
            return map[num[i]], i

    return -1, -1

a = [2,4,7,9,5,3,11,8]

result = twoSum(a,13)
print(a[result[0]],a[result[1]])
print("two sum is  ",result)

king = {'kiko':10086,'suzi':20083,'feifei':1995,'beibei':998}
king['zilong'] = 10
print(king)
print(king['kiko'])
print(king.values())
print(king.keys())
#print(king.pop('kiko'))

sort1 = [k for k in sorted(king.values())]
print(sort1)

# in 实在keys中
b = 'kiko' in king
print(b)
c = 10 in king
print(c)