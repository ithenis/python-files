def square(x):
    return x**2

y = square(5)
print y

######################################
ptr = square
print ptr(9)

#######################################
cube = lambda x: x**3

print cube(3)

#######################################
def average(x, y, z):
    return float((x + y + z)/3.0)

print average(6.0,4,9)

#######################################
def quad(x):
    return x**4

def power(fn,x):
    return fn(x)
    
print power(quad,7)
print power(square,7)    
print power(lambda x: x**5,7)    