# import mylib
import mylib as m
from mylib import f2, f3, f4
from mylib import f1 as ff1
# using 'from' is a bad idea
# from mylib import *

def f1():
    print "local f1()"
f1()

ff1()
f2()
f3()
f4()


m.f1()
m.f2()
m.f3()
m.f4()