def volume(**d):
    return d['h']*(d['w']+2)*(d['l']+5)

# print volume(10,20,30)  # pass by position
# print volume(20,10,30)
# print volume(l = 30,w = 20,h = 10)   # pass by name
d = {'l' : 30,'w' : 20,'h' : 10}
print volume(**d)

##################
def f(*args,**kwargs):
    print args
    return (kwargs)


print f(11,22,33,kk=2,ll=5)

#####################
x = 40
print x / 10
print x % 10

if x%10==0:
    print 'x is divisible by 10'
else:
    print "x isn't divisible by 10"