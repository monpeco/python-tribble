#import ctypes
from ctypes import *
#import cinpy
from cinpy import *

#http://stackoverflow.com/questions/4376397/executing-a-c-program-in-python

# Fibonacci in Python
def fibpy(x):
    if x<=1: return 1
    return fibpy(x-1)+fibpy(x-2)

# Fibonacci in C
fibc=cinpy.defc("fib",
                ctypes.CFUNCTYPE(ctypes.c_long,ctypes.c_int),
                """
                long fib(int x) {
                    if (x<=1) return 1;
                    return fib(x-1)+fib(x-2);
                }
                """)

# ...and then just use them...
# (there _is_ a difference in the performance)
print fibpy(30)
print fibc(30)