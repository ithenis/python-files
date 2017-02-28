x = [(20,30), [40,50]]
print x[0][1]
x[1][1] = 99
print x
try:      # don't display the error message
    x[0][1] = 99
except:
    print "can't do that"
    
print x

x[0] = 'hello'
print x