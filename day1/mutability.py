def addOne(x):
    # print id(x)
    x = x + 1
    # print id(x)
    return x    # returns a copy of the pointer
a = 100
# print id(a)
a = addOne(a)
print a



#################################################################
def addEntry(l):
    l.append(99)
    
mylist = [1,2,3]
addEntry(mylist)
print mylist