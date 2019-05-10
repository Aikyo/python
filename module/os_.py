import os
path = os.getcwd()
print(" get current work place :",os.getcwd())
listd = os.listdir(path)
print(" list file name in current work place :",listd)


#当前路径的绝对路径
abspath = os.path.abspath(".")
print(abspath)

#当前路径上级的绝对路径
abspath_ = os.path.abspath("..")
print(abspath_)

#split file and path
path_file = os.path.split(path)
print(path_file)

#get file create modify and access time
modify = os.path.getmtime(path)
create = os.path.getctime(path)
access = os.path.getatime(path)
print(" module's create time is {} the last modify time is {} and access time {}".format(create,modify,access))

print(path)

#get size of the file
size_ = os.path.getsize(path+r"\\os_.py")

print(size_)









