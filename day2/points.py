class Point:
    '''
    This is a 
    Point class
    '''
    count = 0
    # decorator (allows class attributes):
    @staticmethod
    def getCount():
        return Point.count
    
    def __init__(self, x0, y0, name):  # CTOR
        # self, x0, y0, name are local variables
        # all local variables die at the end of the method
        # self.__dict__['x'] = x0
        self.x = x0
        self.y = y0
        self.name = name
        Point.count += 1
    def __del__(self):
        pass
        # do not use !
       
    def get(self):
        print "Point '{2}' is at ({0}, {1})".format(self.x, self.y, self.name)
    
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
     

    

# create 3 objects
print Point.getCount()
p1 = Point(100, 200, 'point-p1')
p2 = Point(110, 250, 'point-p2')
p3 = Point(120, 230, 'point-p3')
print Point.__dict__


# Point.get(p1)
p1.get()

print p1.__dict__
p1.move_by(10,20)

1