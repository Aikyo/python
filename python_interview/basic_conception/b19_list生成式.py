L = ["Tom","Herman",23,"KIKO"]

list1 = [x.lower() if isinstance(x, str) else x for x in L]
print(list1)

list2 = list(map(lambda x : x.lower() if isinstance(x,str) else x in L,L))
list2 = list(map(lambda x: x.lower() if isinstance(x, str) else x,  L))
print(list2)


list3 = list(map(lambda x : x.lower(),filter(lambda x: isinstance(x,str),L)))
list4 = list(map(lambda x: x.lower(), filter(lambda x: isinstance(x, str), L)))
print(list3)


