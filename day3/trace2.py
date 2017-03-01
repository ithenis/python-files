# decorator
#################################################
def trace(fn):
    def bob(x): # this is the functional decorator
        print 'calling {1}({0})'.format(x, fn.__name__)
        return fn(x)
    return bob

# library, with decorator added
#################################################
@trace
def square(x):
    return x**2
@trace
def cube(x):
    return x**3

@trace
def quad(x):
    return x**4


# user
##################################################
print square(6)
print cube(5)
print quad(4)