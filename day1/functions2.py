#variadic function
# * = twinkle
def average(*x):   # * = wrap
    #return (x + y + z)/3.0
    print x
    return float(sum(x))/len(x)

print average(3, 6, 12, 5)
t = (3,6,12,5)

print average(10,*t) # * = unwrap