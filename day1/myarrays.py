import copy

x = [[10,20], [30,40],[50,60],[70,80],[90,100]]

print x[-2]
print x[2:4]


y = x[:]  # default slice (shallow copy)
# print id(x)
# print id(y)

t = tuple(x)
w = list(x)
print t
z = copy.deepcopy(x)
print id(x),id(x[0])
print id(y),id(y[0])
print id(w),id(w[0])
print id(t),id(t[0])
print id(z),id(z[0])

