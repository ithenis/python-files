def trace(fn):
    def bob(x): # this is the functional decorator
        print 'calling {1}({0})'.format(x, fn.__name__)
        return fn(x)
    return bob



def square(x):
    return x**2

def cube(x):
    return x**3


def quad(x):
    return x**4


print trace(square)(6)
print trace(cube)(5)
print trace(quad)(4)