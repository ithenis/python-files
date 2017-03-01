class NumberIsOdd(Exception):
    def __init__(self,x):
        self.x = x
    
    
    
    
class NumberIsNegative(Exception):
    def __init__(self,x):
        self.x = x

def main():
    try:
        part1(105)
        part2(-67)
        part3(3)
        part4(2)
    except Exception as e:
        print e
    
def part1(x):
    try:
        print 'part1'
        if x > 100:
            raise Exception('x is too big for part1')
        
        print 'part1'
    except Exception as e:
        
        if x > 1000:
            raise Exception("x is too big to continue routine")
        else:
            print e
    
    
    
def part2(x):
    try:
        print 'part2'
        if x < 0:
            raise NumberIsNegative(x)
        if x % 2 ==1:
            raise NumberIsOdd(x)    
        
        print 'part2'
    except NumberIsOdd as e:
        print 'Number is odd'
    except NumberIsNegative as e:
        print 'Number is negative'    
        
def part3(x):
    print 'part3'
    
    print 'part3'
def part4(x):
    print 'part4'
    print 'part4'

main()