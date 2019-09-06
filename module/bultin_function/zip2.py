lst1 = [1,2,3]
lst2 = list('abc')
lst3 = list('RTY')
lst4 = zip(lst1,lst2,lst3)
for i in lst4:
    print(i)

#[x + 1,x+2 for x in lst1]

[x + 2 for x in lst1]


lambda x:x +1

lst5 = list('123')

go = []
go1 = []
def f(x):
    global go,go1
    return go.append(x+1),go1.append(x**2)
maped = map(int,lst5)
print(maped)
print(list(maped))

ls = map(lambda x:x+1,lst1)
print(list(ls))

ls = map(f,lst1)
print(list(ls))
print(go,go1)




