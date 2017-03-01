class Fibonacci:
    def __init__(self):
        self.x = 0
        self.y = 1
        
    def __iter__(self):
        return self
    
    def next(self):
        self.x, self.y = self.y, self.x+self.y
        if self.y > 100:
            raise StopIteration()  # equivalent to return in Matlab
        
        return self.y


    
########################################
        
f = Fibonacci()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()

# __init__ is called first, then it calls __iter__ and then 
# repeats calls to next    
for x in Fibonacci():
    print x